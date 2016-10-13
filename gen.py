#! /usr/bin/python
import xml.etree.ElementTree
import sys
import textwrap

def formatAsComment(text, indents, width=80):
  text = textwrap.dedent(text)
  textList = textwrap.wrap(text, width-3 - 2*indents)
  textList = map(lambda x: "  "*indents+"// "+x, textList)
  return '\n'.join(textList)

class Module:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.registers = []

  def getRegisterStructs(self):
    string = ""
    for register in self.registers:
      string += register.getStruct()
    return string

  def getTypeName(self):
    return self.name + "_regdef_t"

  def getStruct(self):
    string = "typename struct " + self.getTypeName()+"{\n"
    for register in self.registers:
      string += (
	"  " +
	register.getTypeName() +
	" " +
	register.name +
	";\n"
      )
    string += "}\n\n"
    return string

  def getDefines(self, commented):
    string = ""
    for register in self.registers:
      string += register.getDefines(commented)
    return string

  def getHeaderFileText(self, commented):
    define =  "_"+ self.name.upper()+"_REGDEF_H_"
    string = ""
    string += "#ifndef " + define + "\n"
    string += "#define " + define + "\n\n"
    string += self.getDefines(commented) + "\n"
    string += self.getRegisterStructs()
    string += self.getStruct()
    string += "#endif\n\n"
    return string

  def getMarkdown(self):
    string = "##%s\n---\n%s\n\n```c\n%s\n```\n\n"%(self.name, self.description, self.getStruct())
    for register in self.registers:
      string += register.getMarkdown()
    return string

class Register:
  def __init__(self, module, name, offset, description):
    self.module = module
    self.name = name
    self.offset = offset
    self.description = description
    self.fields=[]

  def getTypeName(self):
    if self.fields:
      return (
	self.module.name + "_regdef_" + self.name +"_t"
      )
    else:
      return "uint32_t"

  def getStruct(self):
    if not self.fields:
      return ""
    else:
      string = "typedef struct " + self.getTypeName() + "{\n"
      for field in self.fields:
	string += "  " + field.getStructLine()
      string += "} " + self.getTypeName() + ";\n\n"
      return string

  def getDefines(self, commented):
    string = ""
    for field in self.fields:
      string += field.getDefines(commented)
    return string

  def getMarkdown(self):
    string = "###%s (offset: %s)\n---\n%s\n\n"%(self.name, self.offset, self.description)
    if self.fields:
      string += "```c\n%s\n```\n\n"%(self.getStruct())
      for field in self.fields:
	string += field.getMarkdown()
    return string

class Field:
  def __init__(self, register, name, size, description):
    self.register = register
    self.name = name
    self.size = size
    self.description = description
    self.values=[]

  def getDefines(self, commented):
    defines = ""
    for value in self.values:
      defines += value.getDefine(commented)
    return defines

  def getStructLine(self):
    return "uint32_t " + self.name + " :"+self.size +";\n"

  def getMarkdown(self):
    string = "#### %s (%s bit)\n%s\n\n"%(self.name, self.size, self.description)
    for value in self.values:
      string += value.getMarkdown() + "\n\n"
    return string


class Value:
  def __init__(self, field, name, val, description):
    self.field = field
    self.name = name
    self.val = val
    self.description = description

  def getQualifiedName(self):
    string = (self.field.register.module.name.upper() +
    "_REGDEF_" +
    self.field.register.name.upper() +
    "_" +
    self.field.name.upper() +
    "_" +
    self.name.upper())
    return string

  def getDefine(self, commented):
    string = ""
    if commented:
      string += "\n" + formatAsComment(self.description, 0) + "\n"
    return string + "#define " + self.getQualifiedName() + " " + self.val + "\n"

  def getMarkdown(self):
    return "**`%s`**: %s\n"%(self.getQualifiedName(), self.description)

def xmlToTree(xmlText):
  xModule = xml.etree.ElementTree.fromstring(xmlText)
  if xModule.tag != "module":
    raise ValueError("Top Level tag must be <module>")
  if not xModule.attrib.get("name", None):
    raise ValueError("module must have a 'name' attribute!")
  module = Module(xModule.attrib['name'], xModule.text)

  for xRegister in xModule:
    if xRegister.tag != "register":
      raise ValueError("Module can only have registers within it!")
    if not xRegister.attrib.get("name", None):
      raise ValueError("Register must have a 'name' attribute!")
    if not xRegister.attrib.get("offset"):
      raise ValueError("Register %s must have an 'offset' attribute"
      %(xregister.attrib['name']))
    register = Register(
      module,
      xRegister.attrib['name'],
      xRegister.attrib['offset'],
      xRegister.text
    )
    module.registers.append(register)

    for xField in xRegister:
      if xField.tag != 'field':
	raise ValueError("registers can contain only field tags!")
      if not xField.attrib.get('name', None):
	raise ValueError("Field with no name in register %s"%(register.name))
      field = Field(
	register,
	xField.attrib['name'],
	xField.attrib.get("size","1"),
	xField.text
      )
      register.fields.append(field)

      for xValue in xField:
	if xValue.tag != "value":
	  raise ValueError("Fields can contain only value tags!")
	if not xValue.attrib.get("name", None):
	  raise ValueError("Value tag must have name in field %s in register %s"%(field.name,
	  register.name))
	if not xValue.attrib.get("val", None):
	  raise ValueError("Value tag named %s in field %s in register %s must have 'val' attibute!"%(xValue.arrib['name'], field.name, register.name))
	value = Value(field, xValue.attrib['name'], xValue.attrib['val'],
	xValue.text)
	field.values.append(value)

  return module

if __name__ == "__main__":
  # Flags
  # -h: help
  # -d: documentation (Unimplemented)
  # -c: comments, produces commented version of the code
  flagDict = {'-h': False, '-d': False, '-c': False}
  flag_list = sys.argv[1:]
  for flag in flag_list:
    if flag not in flagDict.keys():
      print "Error, unrecognized flag %s, try\n %s -h \nfor more info\n"%(flag,
      sys.argv[0])
      exit()
    flagDict[flag] = True
    
  if flagDict['-h']:
    print """
      The xml generator takes xml from stdin and outputs c header file text
    in stdout.
      -h: show this help text
      -c: generate a commented version of the code
      -d: generate documentation instead of c code (not yet implemented)

    """
  elif flagDict['-d']:
    tree = xmlToTree(sys.stdin.read())
    print tree.getMarkdown()
  else:
    tree = xmlToTree(sys.stdin.read())
    print tree.getHeaderFileText(flagDict['-c'])


#ifndef _GPIO_REGDEF_H_
#define _GPIO_REGDEF_H_


typedef struct GPIO_regdef_DAT_t{
  uint32_t DAT0 :1;
  uint32_t DAT1 :1;
  uint32_t DAT2 :1;
  uint32_t DAT3 :1;
  uint32_t DAT4 :1;
  uint32_t DAT5 :1;
  uint32_t DAT6 :1;
  uint32_t DAT7 :1;
} GPIO_regdef_DAT_t;

typedef struct GPIO_regdef_DDR_t{
  uint32_t DDR0 :1;
  uint32_t DDR1 :1;
  uint32_t DDR2 :1;
  uint32_t DDR3 :1;
  uint32_t DDR4 :1;
  uint32_t DDR5 :1;
  uint32_t DDR6 :1;
  uint32_t DDR7 :1;
} GPIO_regdef_DDR_t;

typedef struct GPIO_regdef_GIE_t{
  uint32_t GIE0 :1;
  uint32_t GIE1 :1;
  uint32_t GIE2 :1;
  uint32_t GIE3 :1;
  uint32_t GIE4 :1;
  uint32_t GIE5 :1;
  uint32_t GIE6 :1;
  uint32_t GIE7 :1;
} GPIO_regdef_GIE_t;

typedef struct GPIO_regdef_GPE_t{
  uint32_t GPE0 :1;
  uint32_t GPE1 :1;
  uint32_t GPE2 :1;
  uint32_t GPE3 :1;
  uint32_t GPE4 :1;
  uint32_t GPE5 :1;
  uint32_t GPE6 :1;
  uint32_t GPE7 :1;
} GPIO_regdef_GPE_t;

typedef struct GPIO_regdef_GNE_t{
  uint32_t GNE0 :1;
  uint32_t GNE1 :1;
  uint32_t GNE2 :1;
  uint32_t GNE3 :1;
  uint32_t GNE4 :1;
  uint32_t GNE5 :1;
  uint32_t GNE6 :1;
  uint32_t GNE7 :1;
} GPIO_regdef_GNE_t;

typedef struct GPIO_regdef_GIS_t{
  uint32_t GIS0 :1;
  uint32_t GIS1 :1;
  uint32_t GIS2 :1;
  uint32_t GIS3 :1;
  uint32_t GIS4 :1;
  uint32_t GIS5 :1;
  uint32_t GIS6 :1;
  uint32_t GIS7 :1;
} GPIO_regdef_GIS_t;

typedef struct GPIO_regdef_GIC_t{
  uint32_t GIC0 :1;
  uint32_t GIC1 :1;
  uint32_t GIC2 :1;
  uint32_t GIC3 :1;
  uint32_t GIC4 :1;
  uint32_t GIC5 :1;
  uint32_t GIC6 :1;
  uint32_t GIC7 :1;
} GPIO_regdef_GIC_t;

typename struct GPIO_regdef_t{
  GPIO_regdef_DAT_t DAT;
  GPIO_regdef_DDR_t DDR;
  GPIO_regdef_GIE_t GIE;
  GPIO_regdef_GPE_t GPE;
  GPIO_regdef_GNE_t GNE;
  GPIO_regdef_GIS_t GIS;
  GPIO_regdef_GIC_t GIC;
}

#endif



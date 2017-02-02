#ifndef _PWM_REGDEF_H_
#define _PWM_REGDEF_H_


typedef struct PWM_regdef_PWME_t{
  uint32_t PWME0 :1;
  uint32_t PWME1 :1;
  uint32_t PWME2 :1;
  uint32_t PWME3 :1;
  uint32_t PWME4 :1;
  uint32_t PWME5 :1;
  uint32_t PWME6 :1;
  uint32_t PWME7 :1;
  uint32_t PWME8 :1;
  uint32_t PWME9 :1;
} PWM_regdef_PWME_t;

typename struct PWM_regdef_t{
  PWM_regdef_PWME_t PWME;
  uint32_t PWMD0;
  uint32_t PWMD1;
  uint32_t PWMD2;
  uint32_t PWMD3;
  uint32_t PWMD4;
  uint32_t PWMD5;
  uint32_t PWMD6;
  uint32_t PWMD7;
  uint32_t PWMD8;
  uint32_t PWMD9;
  uint32_t PWMR0;
  uint32_t PWMR1;
  uint32_t PWMR2;
  uint32_t PWMR3;
  uint32_t PWMR4;
  uint32_t PWMR5;
  uint32_t PWMR6;
  uint32_t PWMR7;
  uint32_t PWMR8;
  uint32_t PWMR9;
  uint32_t PWMC0;
  uint32_t PWMC1;
  uint32_t PWMC2;
  uint32_t PWMC3;
  uint32_t PWMC4;
  uint32_t PWMC5;
  uint32_t PWMC6;
  uint32_t PWMC7;
  uint32_t PWMC8;
  uint32_t PWMR9;
}

#endif



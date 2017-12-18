/**
 * Sensor spec.
 *   5V Supply
 *   Hight/Low
 *   0V Ground
 * http://www.ktman.pe.kr/RaspberryPi/60518
 */
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define PIN_INPUT 1

void initialize() {
  wiringPiSetup();

  pinMode(PIN_INPUT, INPUT);
}

int main(void) {

  initialize();
  while (1) {
    if (digitalRead(PIN_INPUT) == HIGH) {
      printf("Motion detected\n");
    } else {
      printf("No motion\n");
    }

    delay(100);
  }

  return 0;
}

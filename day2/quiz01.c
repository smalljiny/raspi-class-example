/**
 * When a motion is detected, your application should measured
 * the distance between the sensor and the object in front of sensor.
 */
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define PIN_INPUT 1

#define PIN_TRIG 7
#define PIN_ECHO 0

#define DENOMINATOR 58.0f // Formula: uS / 58 = centimeters
#define INITIAL_DELAY 30
#define TRIGGER_PLUSE_TIME 20

static volatile int globalMotionState = 0;

void initialize() {
  wiringPiSetup();

  pinMode(PIN_INPUT, INPUT);

  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);

  digitalWrite(PIN_TRIG, LOW);
  delay(INITIAL_DELAY);
}

void shootTriggerPulse() {
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(TRIGGER_PLUSE_TIME);
  digitalWrite(PIN_TRIG, LOW);
}

float getTravelTime() {
  while(digitalRead(PIN_ECHO) == LOW);
  long startTime = micros();
  while(digitalRead(PIN_ECHO) == HIGH);

  return (float) (micros() - startTime);
}

float getDistance() {
  shootTriggerPulse();

  return (getTravelTime() / DENOMINATOR);
}

void fallingInterrupt() {
  //printf("no motion\n");
  if (digitalRead(PIN_INPUT) == HIGH) {
    globalMotionState = 1;
  } else {
    globalMotionState = 0;
  }
}

void risingInterrupt() {
  printf("motion\n");
  globalMotionState = 1;
}

int main(void) {

  initialize();

  if (wiringPiISR (PIN_INPUT, INT_EDGE_BOTH, &fallingInterrupt) < 0) {
    return 1;
  }


  for (;;) {
    if (globalMotionState) {
      float distance = getDistance();
      printf("Distance: %0.2fcm\n", distance);
    }
    delay(1000);
  }

  return 0;
}

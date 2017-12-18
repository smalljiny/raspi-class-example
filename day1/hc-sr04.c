/**
 * Sensor spec.
 *   5V Supply
 *   Trigger Pulse Input
 *   Echo Pulse Output
 *   0V Ground
 *   Formula: uS / 58 = centimeters or uS / 148 =inch; or:
 *   the range = high level time * velocity (340M/S) / 2;
 *   we suggest to use over 60ms measurement cycle
 */
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define PIN_TRIG 7
#define PIN_ECHO 0

#define DENOMINATOR 58.0f // Formula: uS / 58 = centimeters
#define INITIAL_DELAY 30
#define TRIGGER_PLUSE_TIME 20

void initialize() {
  wiringPiSetup();

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

int main(void) {
    initialize();
    while (1) {
        float distance = getDistance();
        printf("Distance: %0.2fcm\n", distance);
        delay(1000);
    }

    return 0;
}

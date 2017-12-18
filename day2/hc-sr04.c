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
#include <time.h>
#include <wiringPi.h>

#define PIN_TRIG 7
#define PIN_ECHO 0

#define DENOMINATOR 58.0f // Formula: uS / 58 = centimeters
#define INITIAL_DELAY 30
#define TRIGGER_PLUSE_TIME 20

typedef struct _Data {
  time_t time;
  float distance;
} Data;

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

int main(int argc, char **argv) {
  FILE *out;

  if (argc != 2) {
      fprintf(stderr, "Usage: fcopy file1 file2\n");
      return -1;
  }

  if ((out = fopen(argv[1], "w")) == NULL) {
      perror(argv[1]);
      return -1;
  }

  initialize();

  for (int i = 0; i < 60; i++) {
    Data data;
    data.distance = getDistance();
    time(&(data.time));

    printf("Distance: %0.2fcm\n", data.distance);
    printf("time : %u\n", (unsigned)(data.time));

    for (int i = 0; i < 3; i++) {
      fwrite(&data, sizeof(Data), 1, out);
    }

    delay(1000);
  }

  fclose(out);

  return 0;
}

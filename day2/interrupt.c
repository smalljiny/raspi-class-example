#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>

#define BUTTON_PIN 4
static volatile int globalCounter = 0;

void myInterrupt (void) {
  ++globalCounter;
}

int main (void) {
  int myCounter = 0;
  if (wiringPiSetupGpio() < 0) {
    return 1;
  }

  if (wiringPiISR (BUTTON_PIN, INT_EDGE_FALLING, &myInterrupt) < 0) {
    return 1;
  }

  for (;;) {
    printf("Waiting...");
    fflush (stdout);

    while (myCounter == globalCounter) {
      delay (100);
    }
    printf ("counter : %d\n", globalCounter);
    myCounter = globalCounter;
  }
  return 0;
}

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include <stdlib.h>
#include <wiringPi.h>

#define UDP_PORT  5100

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

int main(int argc, char** argv){
   int sockfd, n;
   socklen_t clisize;
   struct sockaddr_in servaddr, cliaddr;
   char sendline[BUFSIZ];
   char recvline[BUFSIZ];

   if(argc != 2) {
      printf("usage : %s <IP address>\n", argv[0]);
      return -1;
   }

   sockfd = socket(AF_INET, SOCK_DGRAM, 0);

   /* 서버의 주소와 포트 번호를 이용해서 주소 설정 */
   bzero(&servaddr, sizeof(servaddr));
   servaddr.sin_family = AF_INET;
   servaddr.sin_addr.s_addr = inet_addr(argv[1]);
   servaddr.sin_port = htons(UDP_PORT);

   initialize();

   while (1) {
     sockfd = socket(AF_INET, SOCK_DGRAM, 0);

     /* 서버의 주소와 포트 번호를 이용해서 주소 설정 */
     bzero(&servaddr, sizeof(servaddr));
     servaddr.sin_family = AF_INET;
     servaddr.sin_addr.s_addr = inet_addr(argv[1]);
     servaddr.sin_port = htons(UDP_PORT);

     float distance = getDistance();
     sendto(sockfd, &distance, sizeof(distance), 0,
           (struct sockaddr *)&servaddr, sizeof(servaddr));
     printf("Distance: %0.2fcm\n", distance);
     delay(1000);

     close(sockfd);
   }

   return 0;
}

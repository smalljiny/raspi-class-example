include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define UDP_PORT  5100

int main(int argc, char** argv)
{
   int sockfd,n;
   struct sockaddr_in servaddr, cliaddr;
   socklen_t len;
   float distance;;

   sockfd = socket(AF_INET, SOCK_DGRAM, 0);

   /* 접속되는 클라이언트를 위한 주소 설정 후 운영체제에 서비스 등록 */
   bzero(&servaddr, sizeof(servaddr));
   servaddr.sin_family = AF_INET;
   servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
   servaddr.sin_port = htons(UDP_PORT);
   bind(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));

   /* 클라이언트로부터 메시지를 받아서 다시 클라이언트로 전송 */
   do {
      len = sizeof(cliaddr);
      n = recvfrom(sockfd, &distance, sizeof(distance), 0, (struct sockaddr *)&cliaddr, &len);
      printf("Received data : %0.2f\n", distance);
   } while(1);

   close(sockfd);

   return 0;
}

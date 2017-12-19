#include <stdio.h>
#include <string.h>
#include <time.h>

typedef struct _Data {
  time_t time;
  float distance;
} Data;

int readFile(char* file) {
  FILE *in;
  int n = 0;

  if ((in = fopen(file, "r")) == NULL) {
      perror(file);
      return -1;
  }

  Data data;
  memset(&data, sizeof(data), 0x00);
  while ((n = fread(&data, sizeof(data), 1, in)) > 0) {
    printf("Distance: %0.2fcm\n", data.distance);
    printf("time : %u\n", (unsigned)(data.time));
    memset(&data, sizeof(data), 0x00);
  }
}

int main(int argc, char **argv)
{
  if (argc != 2) {
      fprintf(stderr, "Usage: fcopy file1 file2\n");
      return -1;
  }

  if (readFile(argv[1]) < 0) {
    fprintf(stderr, "reading failed\n");
    return -1;
  }

  return 0;
}

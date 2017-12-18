#include <stdio.h>
#include <string.h>

typedef struct _Data {
  int id;
  float temp;
} Data;

int saveFile(char* file) {
  Data datas[] = {
    {1, 100.0f},{2, 777.7f},{3, 200.3f}
  };

  FILE *out;

  if ((out = fopen(file, "w")) == NULL) {
      perror(file);
      return -1;
  }

  for (int i = 0; i < 3; i++) {
    fwrite(&datas[i], sizeof(Data), 1, out);
  }

  fclose(out);

  return 0;
}

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
    printf("%d : %0.1f\n", data.id, data.temp);
    memset(&data, sizeof(data), 0x00);
  }
}

int main(int argc, char **argv)
{
  if (argc != 2) {
      fprintf(stderr, "Usage: fcopy file1 file2\n");
      return -1;
  }

  if (saveFile(argv[1]) < 0) {
    fprintf(stderr, "writing failed\n");
    return -1;
  }

  if (readFile(argv[1]) < 0) {
    fprintf(stderr, "reading failed\n");
    return -1;
  }

  return 0;
}

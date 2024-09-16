#include <stdio.h>
#include <stdlib.h>

int main(void) {
  FILE* f;

  f = fopen("hello.txt", "r");
  int c;
  if (f) {
    while((c = fgetc(f)) != EOF) {
      printf("%c", c);
    }
  }
  fclose(f);

  FILE *fd;
  char s[1024];
  int linecount = 0;

  fd = fopen("quote.txt", "r");
  while(fgets(s, sizeof s, fd) != NULL) {
    printf("%d: %s", ++linecount, s);
  }
  fclose(fd);

  FILE *w = fopen("whales.txt", "r");
  char name[1024];
  float length;
  int mass;

  if (!w) {
    exit(1);
  }

  while(fscanf(w, "%s %f %d", name, &length, &mass) != EOF) {
    printf("%s whale, %d tonnes, %.1f meters\n", name, mass, length);
  }
  fclose(w);

  FILE *fp;
  int x = 32;

  fp = fopen("output.txt", "w");
  if(!fp) {
    exit(1);
  }

  fputc('B', fp);
  fputc('\n', fp);
  fprintf(fp, "x = %d\n", x);
  fputs("Hello, World!\n", fp);

  fclose(fp);

  FILE *b = fopen("bin.txt", "wb");
  unsigned char bytes[6] = { 5, 37, 0, 87, 255, 12 };
  fwrite(bytes, sizeof(char), 6, b);
  fclose(b);

  FILE *rb = fopen("bin.txt", "rb");
  if(!rb) {
    exit(1);
  }
  unsigned char bc;

  while(fread(&bc, sizeof(char), 1, b) > 0) {
    printf("%d\n", bc);
  }

}

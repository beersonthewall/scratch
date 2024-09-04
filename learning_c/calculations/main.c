#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const char* usage = "Usage:\n calc {sum, product, mean} [nums]\nExample:\n calc sum [1,2,3]\n";

int main(int argc, char* argv[]) {
  if(argc != 3) {
    fprintf(stderr, "%s", usage);
    exit(EXIT_FAILURE);
  }

  char* fst = argv[1];
  //char* snd = argv[2];

  if(strcmp(fst, "sum") == 0) {
    printf("sum\n");
  }
}

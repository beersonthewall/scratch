#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const char* usage = "Usage:\n calc {sum, product, mean} [nums]\nExample:\n calc sum [1,2,3]\n";

// define our own because: https://nullprogram.com/blog/2023/02/11/
bool xisdigit(char c) {
  return c>='0' && c <='9';
}

int parse_numbers(char* input, int* numbers) {
  size_t len = strlen(input);
  size_t current_num = 0;
  for(size_t i = 0; i < len; i++) {
    char c = input[i];

    if(!xisdigit(c)) {
      continue;
    }

    size_t digit_start = i;
    size_t j = i;
    while(xisdigit(input[j]) && j < len) { j += 1; }
    char old = input[j];
    input[j] = '\0';
    printf("parsing: %s\n", &input[digit_start]);
    numbers[current_num] = atoi(&input[digit_start]);
    input[j] = old;
    current_num++;
  }

  return 0;
}

int main(int argc, char* argv[]) {
  if(argc != 3) {
    fprintf(stderr, "%s", usage);
    exit(EXIT_FAILURE);
  }

  char* fst = argv[1];
  char* snd = argv[2];

  // The length of the input string will be more than enough to cover the
  // number of int's we need.
  int* numbers = malloc(sizeof(int) * strlen(snd));
  if( parse_numbers(snd, numbers) || numbers == NULL ) {
    fprintf(stderr, "Failure parsing numbers");
    exit(EXIT_FAILURE);
  }

  for(size_t i = 0; i < strlen(snd); i++) {
    printf("%d", numbers[i]);
  }

  if(strcmp(fst, "sum") == 0) {
    printf("sum\n");
  }

  return 0;
}

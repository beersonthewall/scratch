#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
  unsigned int low;
  unsigned int high;
  char letter;
  char* password;
} PASSWORD;

void* safe_malloc(size_t n) {
  void* p = malloc(n);
  if(p == NULL) {
    fprintf(stderr, "Fatal: failed to allocate %zu bytes.\n", n);
    abort();
  }
  return p;
}

PASSWORD** parse_input(char* filename, int* len) {
  FILE* file = fopen(filename, "r");

  if(file == 0) {
    perror(filename);
    abort();
  }


  unsigned int capacity = 100;
  unsigned int length = 1;
  PASSWORD** input = safe_malloc(capacity * sizeof(PASSWORD*));

  PASSWORD* current = (PASSWORD*) safe_malloc(sizeof(PASSWORD));

  const unsigned int buffer_size = 80;
  char buffer[buffer_size];

  while(fscanf(file, "%u-%u %c: %s", &current->low, &current->high,
               &current->letter, buffer) != EOF) {
    current->password = strdup(buffer);
    memset(buffer, ' ', buffer_size);

    input[length-1] = current;
    current = (PASSWORD*) safe_malloc(sizeof(PASSWORD));
    length++;
    if(length == capacity) {
      capacity *= 2;
      input = realloc(input, capacity * sizeof(PASSWORD*));
      if(input == NULL) {
        fprintf(stderr, "Fatal: failed to allocate %zu bytes.\n", capacity * sizeof(PASSWORD*));
        abort();
      }
    }
  }

  fclose(file);
  length--;
  *len = length;
  return input;
}

bool validate(PASSWORD* password) {
  char* pw = password->password;
  size_t len = strlen(pw);
  unsigned int count = 0;
  for(int i = 0; i < len; ++i) {
    if(pw[i] == password->letter) {
      ++count;
    }
  }

  return count >= password->low && count <= password->high;
}

bool validate_position(PASSWORD* password) {
  char* pw = password->password;
  unsigned int low = password->low - 1;
  unsigned int high = password->high - 1;
  return !(pw[low] == password->letter && pw[high] == password->letter)
    && (pw[low] == password->letter || pw[high] == password->letter);
}

int main(int argc, char* argv[]) {

  char* filename = "input/day2.txt";
  int length = 0;
  PASSWORD** input = parse_input(filename, &length);

  unsigned int valid_count = 0;
  unsigned int p2_valid_count = 0;
  for(int i = 0; i < length; ++i) {
    if(validate(input[i])) {
      valid_count++;
    }
    if(validate_position(input[i])) {
      p2_valid_count++;
    }
  }

  printf("Part 1: There are %u valid passwords.\n", valid_count);
  printf("Part 2: There are %u valid passwords.\n", p2_valid_count);

  for(int i = 0; i < length; ++i) {
    free(input[i]);
  }

  free(input);
  return 0;
}

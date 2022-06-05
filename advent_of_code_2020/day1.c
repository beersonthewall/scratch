#include <stdlib.h>
#include <stdio.h>
#include <string.h>

# define BUFFER_SZ = 80;

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main(int argc, char* argv[]) {
  char* filename = "input/day1.txt";
  FILE* file = fopen(filename, "r");

  if (file == NULL) {
    perror(filename);
    exit(EXIT_FAILURE);
  }

  char* line = NULL;
  size_t len = 0;
  size_t inputLen = 1;
  int* input = malloc(inputLen * sizeof(int));

  while(getline(&line, &len, file) != -1) {
    line[strcspn(line, "\r\n")] = 0;
    input[inputLen-1] = atoi(line);
    inputLen++;
    input = realloc(input, inputLen * sizeof(int));
  }

  // part 1
  int part1 = 0;
  for(int i = 0; i < inputLen; ++i) {
    for(int j = 0; j < inputLen; ++j) {
      if(input[i] != input[j] && input[i] + input[j] == 2020) {
        part1 = input[i] * input[j];
        printf("Part 1: %d * %d = %d\n", input[i], input[j], input[i] * input[j]);
        break;
      }
    }
    if(part1 != 0) {
      break;
    }
  }

  // part 2
  qsort(input, inputLen, sizeof(int), cmpfunc);
  for(int i = 1; i < inputLen-2; ++i) {
      int low = 0;
      int high = inputLen - 1;
      while(low != high) {
        int sum = input[i] + input[low] + input[high];
        if(sum > 2020) {
          high--;
        }else if(sum < 2020) {
          low++;
        }else {
          printf("Part 2: %d * %d * %d = %d\n", input[i], input[low], input[high], input[i] * input[low] * input[high]);
          return 0;
        }
      }
  }

  free(input);
  fclose(file);
  printf("No solution found.\n");
  return 1;
}

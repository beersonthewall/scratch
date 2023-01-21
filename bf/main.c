#include <stdio.h>
#include <stdlib.h>

const int NCELLS = 65536;

void inc(int* index) {
  *index += 1;

  if(*index >= NCELLS)
    *index = 0;
}

void dec(int* index) {
  *index -= 1;

  if(*index < 0)
    *index = NCELLS - 1;
}

void forward_jump(char* program, long program_sz, long* program_counter) {
  long count = 0;
  while(*program_counter < program_sz) {
    if(program[*program_counter] == '[') {
      count++;
    } else if(program[*program_counter] == ']') {
      count--;
    }

    if(count == 0) {
      return;
    }

    *program_counter += 1;
    *program_counter = *program_counter % program_sz;
  }
}

void backward_jump(char* program, long program_sz, long* program_counter) {
  long count = 0;
  while(*program_counter >= 0) {
    if(program[*program_counter] == ']') {
      count++;
    } else if(program[*program_counter] == '[') {
      count--;
    }

    if(count == 0) {
      return;
    }

    *program_counter -= 1;
    if(program_counter < 0)
      *program_counter = program_sz - 1;
  }
}

int main(int argc, char* argv[]) {
  if(argc != 2) {
    printf("Usage: bf <filename>\n");
    return -1;
  }

  char* cells = calloc(NCELLS, sizeof(char));

  if(cells == NULL)
    return -1;

  FILE* fd = fopen(argv[1], "r");

  if(fseek(fd, 0, SEEK_END))
    return -1;

  long input_sz = ftell(fd);
  rewind(fd);

  char* program = calloc(input_sz, sizeof(char));
  if(program == NULL)
    return -1;

  long i = 0;
  char c;
  while((c = getc(fd)) != EOF) {
    program[i] = c;
    i += 1;
  }

  long program_sz = i + 1;
  program = realloc(program, program_sz);
  if(program == NULL)
    return -1;

  int cells_index = 0;
  long program_counter = 0;

  while(program_counter < program_sz) {
    switch(program[program_counter]) {
    case '>':
      inc(&cells_index);
      break;
    case '<':
      dec(&cells_index);
      break;
    case '+':
      cells[cells_index] += 1;
      break;
    case '-':
      cells[cells_index] -= 1;
      break;
    case '.':
      putchar(cells[cells_index]);
      break;
    case ',':
      cells[cells_index] = getchar();
      break;
    case '[':
      if(cells[cells_index] == 0) {
        forward_jump(program, program_sz, &program_counter);
      }
      break;
    case ']':
      if(cells[cells_index] != 0) {
        backward_jump(program, program_sz, &program_counter);
      }
      break;
    default:
      break;
    }

    program_counter += 1;
  }

  fclose(fd);
  free(cells);
  free(program);

  return 0;
}

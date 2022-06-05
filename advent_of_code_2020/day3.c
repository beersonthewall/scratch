#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define BUFFER_WIDTH 31

void* safe_malloc(size_t n) {
  void* p = malloc(n);
  if(p == NULL) {
    fprintf(stderr, "Fatal: failed to allocate %zu bytes.\n", n);
    abort();
  }
  return p;
}

// Converts from string to array of bools.
// Uses convention '.' == true and '#' == false.
bool* convert(char* buffer) {
  bool* graph_line = safe_malloc(BUFFER_WIDTH * sizeof(bool));
  for(int i = 0; i < BUFFER_WIDTH; ++i) {
    if(buffer[i] == '.') {
      graph_line[i] = true;
    } else {
      graph_line[i] = false;
    }
  }
  return graph_line;
}

bool** parse_input(char* filename, unsigned int* l) {
  FILE* file = fopen(filename, "r");
  if(file == NULL) {
    perror(filename);
    abort();
  }

  unsigned int capacity = 100;
  unsigned int length = 0;
  bool** graph = safe_malloc(capacity * sizeof(bool*));
  char* buffer = safe_malloc(BUFFER_WIDTH * sizeof(char));
  size_t len = 31;
  while(getline(&buffer, &len, file) != -1) {
    bool* graph_line = convert(buffer);
    graph[length] = graph_line;
    length++;

    if(length == capacity) {
      capacity *= 2;
      graph = realloc(graph, capacity * sizeof(bool*));
      if(graph == NULL) {
        fprintf(stderr, "Fatal: failed to reallocate graph.\n");
        abort();
      }
    }
  }

  graph = realloc(graph, length * sizeof(bool*));
  if(graph == NULL) {
    fprintf(stderr, "Fatal: failed to reallocate graph.\n");
    abort();
  }
  *l = length;
  return graph;
}

unsigned int check_slope(bool** graph, unsigned int length,
                         unsigned int dx, unsigned int dy) {
  unsigned int tree_ct = 0;
  for(unsigned int y = 0; y < length; y += dy) {
    unsigned int x = ((y / dy) * dx);
    // Imitate our input continuing into infinity in the x direction
    // by using x modulo the initial width.
    bool value = graph[y][x % BUFFER_WIDTH];
    printf("x: %u, y: %u, x mod 31: %u, open? %u\n", x, y, x % BUFFER_WIDTH, value);
    if(!value) {
      tree_ct++;
    }
  }  
  return tree_ct;
}

int main(int argc, char* argv[]) {
  char* filename = "input/day3.txt";
  // Chosen the convention '.' is true, '#' is false
  unsigned int length = 0;
  bool** graph = parse_input(filename, &length);

  unsigned int p1 = check_slope(graph, length, 3, 1);
  unsigned int a = check_slope(graph, length, 1, 1);
  unsigned int b = check_slope(graph, length, 5, 1);
  unsigned int c = check_slope(graph, length, 7, 1);

  unsigned int d = check_slope(graph, length, 1, 2);
  unsigned long long result = p1 * a * b * c * d;
  printf("Part 1: You will encounter %u trees.\n", p1);
  printf("Part 2: %u * %u * %u * %u * %u = %llu\n",
         p1, a, b, c, d, result);

  // clean up clean up, everyone do you share.
  for(int i = 0; i < length; ++i) {
    free(graph[i]);
  }
  free(graph);
  return 0;
}

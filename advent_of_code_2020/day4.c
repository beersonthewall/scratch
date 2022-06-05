#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
  unsigned int birth_year;
  unsigned int issue_year;
  unsigned int expire_year;
  unsigned int height;
  char* hair_clr;
  char* eye_clr;
  unsigned int id;
  unsigned int country_id;
} PASSPORT;

void* safe_malloc(size_t n) {
  void* p = malloc(n);
  if(p == NULL) {
    fprintf(stderr, "Fatal: failed to allocate %zu bytes.\n", n);
    abort();
  }
  return p;
}

void add_passport_field(PASSPORT* passport, char* key, char* val) {
  if(strcmp("byr", key) == 0) {
    passport->birth_year = atoi(val);
  }else if(strcmp(key, "iyr") == 0) {
    passport->issue_year = atoi(val);
  }else if(strcmp(key, "eyr") == 0) {
    passport->expire_year = atoi(val);
  }else if(strcmp(key, "hgt") == 0) {
    passport->height = atoi(val);
  }else if(strcmp(key, "hcl") == 0) {
    size_t l = strlen(val);
    passport->hair_clr = safe_malloc(l);
    strcpy(passport->hair_clr, val);
  }else if(strcmp(key, "ecl") == 0) {
    size_t l = strlen(val);
    passport->eye_clr = safe_malloc(l);
    strcpy(passport->eye_clr, val);
  }else if(strcmp(key, "pid") == 0) {
    passport->id = atoi(val);
  }else if(strcmp(key, "cid") == 0) {
    passport->id = atoi(val);
  }else {
    fprintf(stderr, "Unrecognized key: %s with value: %s", key, val);
    abort();
  }

}

PASSPORT** parse_input(char* filename, unsigned int* l) {
  FILE* file = fopen(filename, "r");
  if(file == NULL) {
    perror(filename);
    abort();
  }

  unsigned int capacity = 100;
  unsigned int length = 0;
  PASSPORT** passports = safe_malloc(capacity * sizeof(PASSPORT*));
  PASSPORT* current = safe_malloc(sizeof(PASSPORT));

  size_t len = 0;
  char* buf = NULL;
  ssize_t nread;

  while((nread = getline(&buf, &len, file)) != -1) {
    if(nread == 1) {
      passports[length] = current;
      current = safe_malloc(sizeof(PASSPORT));
      length++;
      if(length == capacity) {
	capacity *= 2;
	passports = realloc(passports, capacity * sizeof(PASSPORT*));
	if(passports == NULL) {
	  fprintf(stderr, "Failure reallocating passports.\n");
	  abort();
	}
      }
      continue;
    }


    // replace newline with null termination

    buf[nread-1] = '\0';

    char* kv_pair = strtok(buf, " ");
    while(kv_pair != NULL) {
      char* key;
      char* val;
      key = strtok(kv_pair, ":");
      val = strtok(NULL, "");

      add_passport_field(current, key, val);

      kv_pair = strtok(NULL, " ");
    }

    free(buf);
    len = 0;
    buf = NULL;
  }
  *l = length;
  return passports;
}

int main(int argc, char* argv[]) {

  char* filename = "input/day4.txt";
  unsigned int length = 0;
  PASSPORT** passports = parse_input(filename, &length);

  unsigned int invalid_ct = 0;
  for(int i = 0; i < length; ++i) {
    PASSPORT* p = passports[i];
    if(p->birth_year == 0
       || p->issue_year == 0
       || p->expire_year == 0
       || p->height == 0
       || p->hair_clr == NULL
       || p->eye_clr == NULL
       || p->id == 0
       || p->country_id == 0) {
      invalid_ct++;
    }

    printf("byr: %d iyr: %d eyr: %d hgt: %d id: %d cid: %d",
	   p->birth_year, p->issue_year, p->expire_year, p->height, p->id, p->country_id);
    if(p->hair_clr != NULL) {
      printf(" hcl: %s", p->hair_clr);
    } else {
      printf(" hcl: NULL");
    }
    if(p->eye_clr != NULL) {
      printf(" ecl: %s\n", p->eye_clr);
    }else {
      printf(" ecl: NULL\n");
    }
  }

  printf("l: %u\n", length);
  printf("Part 1: there are %u valid passports.\n", length - invalid_ct);

  for(int i = 0; i < length; ++i) {
    PASSPORT* p = passports[i];
    if(p->hair_clr != NULL) {
      free(p->hair_clr);
    }
    if(p->eye_clr != NULL) {
      free(p->eye_clr);
    }
    free(p);
  }

  free(passports);

  return 0;
}

/*
  unsigned int birth_year;
  unsigned int issue_year;
  unsigned int expire_year;
  unsigned int height;
  char* hair_clr;
  char* eye_clr;
  unsigned int id;
  unsigned int country_id
*/

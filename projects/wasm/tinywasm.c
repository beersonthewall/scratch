#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/* ========= type definitions ========= */

typedef struct Runtime {
} Runtime;

/* ========= end type definitions ========= */

/* ========= leb128 ========= */

int read_u32_leb128(uint32_t* u, FILE *f) {
  *u = 0;
  for(int i = 0; i < 5; i++) {
    uint32_t c = (uint32_t) fgetc(f);
    if(feof(f) || (int)c == EOF) {
      fprintf(stderr, "Unexpected EOF\n");
      return -1;
    }

    //printf("read byte %x\n", c);
    *u |= (c & 0x7f) << (i*7);
    if(!(c & 0x80)) { return 0; }
  }
  return 0;
}

/* ========= end leb128 ========= */

/* ========= begin binary format ========= */

int load_section(Runtime *r, FILE *f) {
  // https://webassembly.github.io/spec/core/binary/modules.html#sections
  int sid = fgetc(f);
  if(feof(f)) {
    fprintf(stderr, "Unexpected EOF\n");
    return -1;
  }
  uint32_t sz = 0;
  if(read_u32_leb128(&sz, f)) {
    return -1;
  }

  fprintf(stderr, "sid: %d, sz: %x\n", sid, sz);

  if(fseek(f, sz, SEEK_CUR)) {
    fprintf(stderr, "fseek err \n");
  }

  switch(sid) {
  case 0: // custom
    break;
  case 1: // type
    break;
  case 2: // import
    break;
  case 3: // function
    break;
  case 4: // table
    break;
  case 5: // memory
    break;
  case 6: // global
    break;
  case 7: // export
    break;
  case 8: // start
    break;
  case 9: // element
    break;
  case 10: // code
    break;
  case 11: // data
    break;
  case 12: // data count
    break;
  default:
    return -1;
    break;
  }
  return 0;
}

// Load a WASM binary into Runtime struct
int load_binary(Runtime* r, FILE* f) {
  unsigned char expected[8] = {
    0x00, 0x61, 0x73, 0x6d,
    0x01, 0x00, 0x00, 0x00,
  };

  // Read magic number and WASM version
  for(size_t i = 0; i < sizeof(expected); i++) {
    char c = (char) fgetc(f);
    if(feof(f) || (int)c == EOF) { return -1; }

    assert(c == expected[i]);
  }

  while(!feof(f)) {
    if(load_section(r, f)) {
      fprintf(stderr, "Failed to load section\n");
      return -1;
    }
  }
  return 0;
}

/* ========= end binary format ========= */

int main(int argc, char **argv) {
  if(argc != 2) {
    fprintf(stderr, "Usage: tinywasm <path-to-binary>\n");
    return 1;
  }

  char* binaryPath = argv[1];
  FILE* f = fopen(binaryPath, "r");
  if(!f) {
    fprintf(stderr, "Error reading binary\n");
    return 1;
  }

  Runtime r = {};
  if(load_binary(&r, f)) {
    return -1;
  }
  fclose(f);
}


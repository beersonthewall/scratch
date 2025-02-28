#include <stdio.h>

int main(void) {
  int a[] = {1,2,3,4,5,6,7,8};
  int *p = &a[0];
  printf("%d\n", *(p + 0));
  const size_t sz = 8;

  for(size_t i = 0; i < sz; i++) {
    printf("%d\n", *(p + i));
  }
}

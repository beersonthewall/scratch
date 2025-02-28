#include <stdio.h>

int main(void) {
  int lower = 0;
  int upper = 300;
  int step = 20;
  float celsius, fahr;

  fahr = lower;

  printf("F\tC\n");
  while(fahr <= upper) {
    celsius = (5.0/9.0) * (fahr - 32.0);
    printf("%3.0f\t%3.1f\n", fahr, celsius);
    fahr = fahr + step;
  }

  celsius = lower;
  printf("C\tF\n");
  while(celsius <= upper) {
    fahr = ((9.0/5.0) * celsius) + 32.0;
    printf("%3.0f\t%3.1f\n", celsius, fahr);
    celsius += step;
  }
}

#include <stdio.h>

typedef struct animal {
  char *name;
  int leg_count, speed;
} animal;

// alt: typedef struct animal animal;

int main(void) {
  typedef int antelope;
  antelope x = 100;

  animal moose = { "Moose", 4, 20 };

  printf("Name: %s\n", moose.name);
  printf("Legs: %d\n", moose.leg_count);
  printf("Speed: %d\n", moose.speed);
}

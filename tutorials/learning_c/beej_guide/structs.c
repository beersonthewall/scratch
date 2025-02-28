#include <stdio.h>

struct car {
  char *name;
  float price;
  int speed;
};

void set_price(struct car *c, float new_price) {
  c->price = new_price;
}

int main(void) {
  struct car corolla;
  corolla.name = "Corolla";
  corolla.price = 20000.00;
  corolla.speed = 100;

  printf("Name: %s\n", corolla.name);
  printf("Price: %f\n", corolla.price);
  printf("Speed: %d\n", corolla.speed);

  // struct initializers
  struct car saturn = {.speed=175, .name="Saturn SL/2", .price=16000.99};
  // alt: struct car saturn = {"Saturn SL/2", 1600.99, 175};
  printf("Name: %s\n", saturn.name);
  printf("Price: %f\n", saturn.price);
  printf("Speed: %d\n", saturn.speed);

  set_price(&saturn, 9.99);
  printf("New Price: %f\n", saturn.price);

}

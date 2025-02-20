#include <cstdint>
#include <iostream>

using namespace std;

// square a number
constexpr double sq(double x) { return x * x; }

// Prints the square of 'x'.
void print_sq(double x) { cout << sq(x) << "\n"; }

void increment() {
  int v[] = {0,1,2,3,4,5,6,7,8,9};
  // if we don't want to copy values from v
  // we can have 'x' refer to an element in v
  // '&' means reference to. references are similar to pointers
  // but you don't need to deref with '*' to access the value
  // I assume this happens automatically with references? rather
  // than the deref not happening.
  // Lastly references cannot be made to refer to a different object
  // after initialization.
  for(auto& x : v)
    ++x;
}

int main() {
  double a {1.0}, b {2.3};
  print_sq(a);
  print_sq(b);

  char v[6];
  char* p = &v[3];
  char x = *p;
  cout << x << '\n';

  // Typical for-loops
  int v1[10] = {0,1,2,3,4,5,6,7,8,9};
  for(auto i = 0; i != 10; ++i) {
    cout << v1[i] << ' ';
  }
  cout << '\n';

  // Can also use a range-for-statement:
  // traverses a sequence without manually checking the bounds.
  for(int x : v1) // alternatively (auto x: v1) works
    cout << x << ' ';
  cout << '\n';

  // Allows for swapping in an initializer
  for(int x : {0,1,2,3,4,5,6,7,8,9})
    cout << x << ' ';
  cout << '\n';

  int f = 420;
  int* foo = &f;
  int& fp = *foo;
  cout << fp << '\n';
  fp = 300;
  cout << f << '\n';
  f = 399;
  cout << fp << '\n';
  f = 10'000;
  int& r {f};
  cout << r << '\n';
}

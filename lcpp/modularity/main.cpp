#include "vec.h"
#include <iostream>
#include <stdexcept>

using namespace std;

int main() {
  MyVector v = MyVector(10);
  cout << v.size() << '\n';
  try {
    cout << v[11];
  }
  catch(const out_of_range& e) {
    cerr << e.what() << '\n';
  }
  return 0;
}

#include <iostream>

using namespace std;

// MyVec struct implementation

struct MyVec {
  double* elem;
  int size;
};

void myvec_init(MyVec& v, int size) {
  v.elem = new double[size];
  v.size = size;
  for(auto i = 0; i < size; ++i) {
    v.elem[i] = 0.0;
  }
}

void myvec_destroy(MyVec& v) {
  delete[] v.elem;
}

constexpr double myvec_sum(MyVec& v) {
  auto s {0.0};
  for(auto i=0; i < v.size; ++i) {
    s += v.elem[i];
  }
  return s;
}

// MyVec class

class MyVector {
public:
  MyVector(int s) :_elem{new double[s]},_sz{s} {
    for(auto i = 0; i < _sz; ++i) {
      _elem[i] = 0.0;
    }
  }

  ~MyVector() {
    delete [] _elem;
  }

  double& operator[](int i) { return _elem[i]; }

  int size() { return _sz; }

private:
  double* _elem;
  int _sz;
};

class Foo {
public:
  Foo(int& i) :foo_ref {i} {}
private:
  int& foo_ref;
};

enum class Color { red, blue, green };
enum class Traffic_light { green, yellow, red };

int main() {
  cout << "Welcome to learning user-defined types :)\n";

  MyVec v;
  myvec_init(v, 10);
  cout << myvec_sum(v) << '\n';
  myvec_destroy(v);

  auto m = MyVector(10);
  cout << m.size() << '\n';
  cout << "first: " << m[0] << '\n';

  Color _c = Color::red;
  Traffic_light _t = Traffic_light::green;
  
  return 0;
}

#include "vec.h"
#include <stdexcept>

MyVector::MyVector(int s) {
  if(s < 0) {
    throw std::length_error{"MyVector constructor: negative size"};
  }
  elem = new double[s];
  sz = s;
}

MyVector::~MyVector() { delete[] elem; }

double &MyVector::operator[](int i) {
  if(i < 0 || i >= size()){
    throw std::out_of_range {"Vector::operator[]"};
  }
  return elem[i];
}

int MyVector::size() { return sz; }

#pragma once

class MyVector {
public:
  MyVector(int s);
  ~MyVector();
  double& operator[](int i);
  int size();
 private:
  double* elem;
  int sz;
};

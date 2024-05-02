#include <iostream>
 int main(int argc, char *argv[]) {
 const int SIZE = 5;
 int *ptr = new int[]{10, 20, 30, 40, 50};
 for (int i= 0; i< SIZE; i++) {
 std::cout<< ptr[i] << "\n";
 }
 for (int i= 0; i< SIZE; i++) {
 std::cout<< *(ptr+i) << "\n";
 }
 delete[] ptr;
 return 0;
 }
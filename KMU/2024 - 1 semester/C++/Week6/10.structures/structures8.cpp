 #include <iostream>
 struct Foo {
 int x;
 int y;
 };
 int main(int argc, char *argv[]) {
 int const SIZE = 5;
 Foo arr[SIZE]{};
 for (int i= 0; i< SIZE; ++i) {
 std::cout<< "arr[" << i<< "] = (" << arr[i].x << ", " 
<< arr[i].y
 << ")\n";
 }
 for (int i= 0; i< SIZE; ++i) {
 arr[i].x = i;
 arr[i].y = i* 2;
 }
 for (int i= 0; i< SIZE; ++i) {
 std::cout<< "arr[" << i<< "] = (" << arr[i].x << ", " 
<< arr[i].y
 << ")\n";
 }
 return 0;
 }
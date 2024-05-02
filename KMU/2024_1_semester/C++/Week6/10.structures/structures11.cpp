 #include <iostream>
 int main(int argc, char *argv[]) {
 char ch{'A'};
 std::cout<< ch<< "\n";
 char *p1{&ch};
 char *p2{p1};
 *p2 = 'B';
 std::cout<< ch<< "\n";
 std::cout<< *p1 << "\n";
 std::cout<< *p2 << "\n";
 *p1 = 'C';
 std::cout<< ch<< "\n";
 std::cout<< *p1 << "\n";
 std::cout<< *p2 << "\n";
 ch= 'D';
 std::cout<< ch<< "\n";
 std::cout<< *p1 << "\n";
 std::cout<< *p2 << "\n";
 return 0;
 }
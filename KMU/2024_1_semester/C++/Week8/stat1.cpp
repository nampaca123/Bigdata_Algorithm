#include <iostream>
void foo() {
static int n{0};
std::cout << ++n << ": foo"
<< "\n";
}
void bar() {
static int n{0};
std::cout << ++n << ": bar"
<< "\n";
}
int main(int argc, char *argv[]) {
foo();
foo();
foo();
bar();
bar();
return 0;
}
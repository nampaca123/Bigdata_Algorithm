#include <iostream>
int n{999};

void foo() {
    static int n{0};
    std::cout << ++n << ": foo" << "\n";

    std::cout << "n = " << n << "\n";
    std::cout << "::n = " << ::n << "\n";
}
//firt find tools in own function, then search other tool outside function
int main(int argc, char *argv[]) {
    foo();
    foo();
    std::cout << "n = " << n << "\n";
    return 0;
}
#include <iostream>

int main(int argc, char *argv[]){
    bool b{true};
    char c{'A'};
    int n{10};
    long l{100L};
    float f{3.141592f};
    double p{3.141592};

std::cout << "typeid(b) = " << typeid(b).name() << '\n';
std::cout << "typeid(c) = " << typeid(c).name() << '\n';
std::cout << "typeid(n) = " << typeid(n).name() << '\n';
std::cout << "typeid(l) = " << typeid(l).name() << '\n';
std::cout << "typeid(f) = " << typeid(f).name() << '\n';
std::cout << "typeid(p) = " << typeid(p).name() << '\n';
std::cout << "L is = " << l << '\n';
return 0;
}
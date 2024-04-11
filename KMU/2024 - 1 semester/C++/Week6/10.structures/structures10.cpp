#include <iostream>
//포인터가 전부 8바이트라는 것을 확인하자
int main(int argc, char *argv[]) {
    char c{'A'};
    float f{36.5};
    auto d{3.141592};

    std::cout << c << "\n";
    std::cout << f << "\n";
    std::cout << d << "\n";

    std::cout << sizeof(c) << "\n";
    std::cout << sizeof(f) << "\n";
    std::cout << sizeof(d) << "\n";

    char *pc{&c};
    float *pf{&f};
    auto *pd{&d};

    std::cout << *pc << "\n";
    std::cout << *pf << "\n";
    std::cout << *pd << "\n";

    std::cout << sizeof(pc) << "\n";
    std::cout << sizeof(pf) << "\n";
    std::cout << sizeof(pd) << "\n";

    return 0;
}
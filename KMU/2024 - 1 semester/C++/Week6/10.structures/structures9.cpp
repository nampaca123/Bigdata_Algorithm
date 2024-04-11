#include <iostream>

int main(int argc, char *argv[]) {
    char ch = 'A';
    std:: cout << ch << "\n";
    std:: cout << sizeof(ch) << "\n";

    char *p(&ch);
    std::cout << *p << "\n";
    std::cout << sizeof(p) << "\n"; // 8 byte, 64bit machine

    return 0;
}
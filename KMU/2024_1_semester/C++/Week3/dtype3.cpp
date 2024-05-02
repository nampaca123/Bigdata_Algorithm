#include <iostream>

int main(int argc, char *argv[]){
    bool b = -10;
    std::cout << "b = " << std::boolalpha << b << '\n';
    std::cout << "b = " << b << '\n';

    bool b1{-10};
    std::cout << "b = " << b1 << '\n';

    return 0;
}
#include <iostream>

int main(int argc, char *argv[]) {
    char ch{'A'};
    std::cout << ch << "\n";
    std::cout << (void *)&ch << "\n";

    char *pl{&ch};
    std::cout<<*pl<<'\n';
    std::cout<<(void *)pl<<'\n';
    std::cout<<(void *)&pl<<'\n';
}
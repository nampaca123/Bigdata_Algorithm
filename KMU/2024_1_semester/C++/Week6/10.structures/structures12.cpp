#include <iostream>

int main(int argc, char *argv[]) {
    char ch{'A'};
    std::cout << ch << "\n";
    std::cout << (void *)&ch << "\n";

    char *p{&ch};
    std::cout<< *p << "\n";
    std::cout<< (void *)p << "\n";
    std::cout<< (void *)&p << "\n";

    std::cout<< "\n";
    char **pp{&p};
    std::cout<< **pp << "\n";
    std::cout<< (void *)pp << "\n";
    std::cout<< (void *)*pp << "\n";
    std::cout<< (void *)&pp << "\n";
    
    return 0;
 }
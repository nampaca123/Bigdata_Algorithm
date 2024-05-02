#include <iostream>
int main(int argc, char *argv[]) {
    enum WEEK { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,
Sunday };
    int day;
    std::cin >> day;
    switch (day) {
    case 1:
    case 3:
        std::cout << "c++ Programming"
        << "\n";
    break;
    default:
    std::cout << "free"
    << "\n";}
    return 0;
}
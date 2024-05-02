#include <iostream>
int main(int argc, char *argv[]) {
    enum WEEK { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,
    Sunday };
    std::string arr[]{"Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"};
    std::cout << arr[2] << "\n";
    std::cout << arr[Wednesday] << "\n";
    return 0;
}
#include <iostream>

int cal(int x) {return x+x;}
float cal(float x) {return x+x;}

int main(int argc, char *argv[]) {
    int data{10};
    int res = cal(data);
    std::cout << "cal(" << data << ") = " << res << "\n";

    float v{2.4};
    float re = cal(v);
    std::cout << "cal(" << v << ") = " << re << "\n";
}
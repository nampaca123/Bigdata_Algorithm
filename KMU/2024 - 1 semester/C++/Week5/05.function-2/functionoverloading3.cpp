#include <iostream>

//기본 매개변수 관련, 아무 것도 입력하지 않았을 때 어떠한 현상이 발생하는가?

int cal(int x = 10) { return x + x;}
int cal() {return 200;}

int main(int argc, char *argv[]) {
    int data{10};
    int res = cal(data);
    std::cout << "cal("<<data<<") = " << res << "\n";
    return 0;
}
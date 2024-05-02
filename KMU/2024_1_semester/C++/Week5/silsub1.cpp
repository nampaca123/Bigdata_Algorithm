#include <iostream>
int cal(int BGN, int END);
int main(int argc, char *argv[]) {
    int const BGN{2};
    int const END{6};

    std::cout << "sum = " << cal(BGN, END) << "\n";
}
int cal(int x, int y) {
    int sum = 0;
    int i;
    for (i=x;i<=y;i++){
        sum+=i;
    }
    return sum;
}
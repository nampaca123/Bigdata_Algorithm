#include <iostream>
int calday(int m, int d){
    int sumday[12]{31,29,31,30,31,30,31,31,30,31,30,31};
    int i = 0;
    int sum = 0;

    if (m!=1){
        for (i=0;i<m-1;i++){
            sum= sum + sumday[i];
        }
        sum = sum + d;
    } else {
        sum += d;
    }
    return sum;
    
}

int main(int argc, char *argv[]){
    int m;
    int d;
    std::cin >> m;
    std::cout << " ";
    std::cin >> d;
    std::cout << calday(m, d) << '\n';
    int sumofday = calday(m,d);
    int wday = 0;
    wday = sumofday % 7;
    std::cout << wday << '\n';
}
#include <iostream>

// 입력된 숫자는 double이지만 함수가 받기로 한 숫자는 double인 경우 에러가 발생하는가?
// float으로 넣을 숫자가 없을 경우 함수에서 자동으로 double 타입으로 매핑을 시켜준다, 그러므로 정상적으로 작동된다!

int cal (int x) { return x + x ; }
double cal ( double x ) { return x + x ;}

int main (int argc, char * argv[] ) {
    int data { 10 };
    int res = cal (data) ;
    std::cout << "cal(" << data << ") = " << res << "\n";

    float v{2.4};
    double re = cal (v) ;
    std:: cout << "cal(" << v << ") = " << re << "\n";

    return 0;
}
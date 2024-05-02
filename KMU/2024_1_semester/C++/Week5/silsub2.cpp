#include <iostream>
#include <iomanip>
bool is_odd(int n){
    return n%2 != 0;
}
int main(int argc, char *argv[]){
    int const n{11};
    std::cout<<"is_odd("<<n<<")"<<std::boolalpha<<is_odd(n)<<"\n";
}
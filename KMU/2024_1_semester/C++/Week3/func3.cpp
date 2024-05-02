#include <iostream>

void foo(int data){
    std::cout << "foo:: data = " << data
    << '\n';
    data= 100;
}
int main(int argc, char *argv[]){
    int data{10};
    foo(data);

    std::cout << "main:: data = " << data 
    << '\n';
    return 0;
}
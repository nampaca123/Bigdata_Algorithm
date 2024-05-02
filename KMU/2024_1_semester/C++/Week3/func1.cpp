#include <iostream>
using namespace std;

void foo(int data) {
    cout<<"hello foo!"<< data << '\n';
}
int main(int argc, char *argv[]){
    cout<<"hello function!"<<'\n';
    int data(10);
    foo(data);
    return 0;
}

#include <iostream>

struct {
    int x;
    int y;
}Foo1, Foo2;

int main(int argc, char *argv[]){
    Foo1 foo1{10,20};
    Foo2 foo2{30,40};
    std::cout << "foo1.x = " << foo1.x << "foo1.y = " << foo1.y << '\n';
    std::cout << "foo2.x = " << foo2.x << "foo2.y = " << foo2.y << '\n';
}

#include <iostream>

typedef struct {
    int x;
    int y;
}   Foo1, Foo2;

int main(int argc, char *argv[]) {
    Foo1 foo1{10,20};
    Foo2 foo2{30,40};
    std::cout << "foo1 = (" << foo1.x << ", " << foo1.y << ")\n";
    std::cout << "foo2 = (" << foo2.x << ", " << foo2.y << ")\n";
    return 0;
}
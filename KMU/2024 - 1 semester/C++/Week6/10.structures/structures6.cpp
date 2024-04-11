#include <iostream>

struct Foo{
    int x;
    int y;
};

Foo foo; // global variable
int main(int argc, char *argv[]) {
    std::cout << "foo = (" << foo.x << ", " << foo.y << ")\n";

    Foo foo1; //local variable
    std:: cout << "foo1 = (" << foo1.x << ", " << foo1.y << ")\n";

    return 0;
}
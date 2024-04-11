#include <iostream>

struct Foo {
    int x;
    int y;
};

int main(int argc, char *argv[]) {
    Foo foo{10, 20};
    std::cout << "foo = (" << foo.x << ", " << foo.y << ")\n";

    auto[x,y] = foo;
    std::cout << "auto = (" << x << ", " << y << ")\n";

    return 0;
}
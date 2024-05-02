#include <iostream>

struct Foo {
    int x;
    int y;
};



int main(int argc, char *argv[]) {
    Foo foo1{10, 20};
    std::cout << "foo1.x = " << foo1.x << "\n";
    std::cout << "foo1.y = " << foo1.y << "\n";

    Foo foo1{10, 20};
    std::cout << "foo1.x = " << foo1.x << "\n";
    std::cout << "foo1.y = " << foo1.y << "\n";

    Foo foo = add(foo1, foo2)
}

}
//typedef을 적지 않아도 되며 마지막에 Foo1이나 Foo2와 같은 structure tag를 기립하지 않아야 한다.

#include <iostream>

struct Foo {
    int x;
    int y;
};

int main(int argc, char *argv[]) {
    Foo foo{100, 200};
    
    std::cout << "foo = (" << foo.x << "," << foo.y <<")\n";

    return 0;
}
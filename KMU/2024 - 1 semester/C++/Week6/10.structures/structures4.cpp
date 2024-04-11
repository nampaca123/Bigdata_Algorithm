#include <iostream>
 struct Foo {
    int x;
    int y;
 };
 int main(int argc, char *argv[]) {
    Foo foo1{10, 20};
    Foo foo= foo1;
    
    std::cout<< "foo1 = (" << foo1.x << ", " << foo1.y << ")\n";
    std::cout<< "foo = (" << foo.x<< ", " << foo.y<< ")\n";
    
    foo1.x = 100, foo1.y = 200;
    
    std::cout<< "foo1= (" << foo1.x << ", " << foo1.y << ")\n";
    std::cout<< "foo = (" << foo.x<< ", " << foo.y<< ")\n";
    return 0;
 }
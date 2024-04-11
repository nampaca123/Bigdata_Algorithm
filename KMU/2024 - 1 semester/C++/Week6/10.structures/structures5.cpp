 #include <iostream>
 
 struct Foo {
    int x;
    int y;
 };
 int main(int argc, char *argv[]) {
 Foo foo;
 std::cout<< "foo  = (" << foo.x<< ", " << foo.y<< ")\n";
 Foo foo1{};
 std::cout<< "foo1  = (" << foo1.x << ", " << foo1.y << ")\n";
 Foo foo2 = {};
 std::cout<< "foo2  = (" << foo2.x << ", " << foo2.y << ")\n";
 Foo foo3{1};
 std::cout<< "foo3  = (" << foo3.x << ", " << foo3.y << ")\n";
 Foo foo4 = {2, };
 std::cout<< "foo4  = (" << foo4.x << ", " << foo4.y << ")\n";
 return 0;
 }
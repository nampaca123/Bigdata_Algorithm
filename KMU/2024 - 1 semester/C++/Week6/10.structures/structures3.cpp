 #include <iostream>
 struct Foo {
    int x;
    int y;
 };

int main(int argc, char *argv[]) {
    Foo foo1{10,20};
    Foo foo2 = {30, 40};

    Foo foo3 = {30, 40};
    Foo foo4 = {30, 40};

    std::cout<<"foo1= (" << foo1.x << ", " << foo1.y << ")\n";
    std::cout<<"foo2= (" << foo2.x << ", " << foo2.y << ")\n";
    std::cout<<"foo3= (" << foo3.x << ", " << foo3.y << ")\n";
    std::cout<<"foo4= (" << foo4.x << ", " << foo4.y << ")\n";

    return 0;
}
#include <iostream>
#include "bar.h"
#include "foo.h"

int main(int argc, char *argv[]){
    foo();
    return 0;
}

//In header, other header better not be included
//In header, variable better not be made
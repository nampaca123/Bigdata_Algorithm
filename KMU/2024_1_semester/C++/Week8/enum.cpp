#include <iostream>

int main(int argc, char *argv[]){
    enum Week {Monday=1, Tuesday, Wednesday, Thursday=1, Friday, Saturday, Sunday};


    int day;
    std::cin >> day;

    switch (day){
        case Week::Tuesday:
        case Thursday:
        std::cout << "c++ Programming" << "\n";
        break;

        default:
        std::cout<<"free"<<"\n";
    }
    return 0;

}
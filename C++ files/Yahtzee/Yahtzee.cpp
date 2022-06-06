#include <iostream>
#include <list>
#include <ctime>

int D1(){
    return (rand() % 6) + 1;
}
int D2(){
    return (rand() % 6) + 1;
}

int D3(){
    return (rand() % 6) + 1;
}

int D4(){
    return (rand() % 6) + 1;
}

int D5(){
    return (rand() % 6) + 1;
}

void main(){
    for(int i = 0; i < 10; i++){
    srand(i);
    int Roll = D1();
    std::cout << D1() << D2() << D3() << D4() << D5() << "\n\n";
}
    }

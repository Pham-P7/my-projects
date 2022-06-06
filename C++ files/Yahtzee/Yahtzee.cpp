#include <iostream>
#include <ctime>
#include <string>
using namespace std; 
int D1()
{
    return (rand() % 6) + 1;
}
int D2()
{
    return (rand() % 6) + 1;
}

int D3()
{
    return (rand() % 6) + 1;
}

int D4()
{
    return (rand() % 6) + 1;
}

int D5()
{
    return (rand() % 6) + 1;
}

void main()
{
    std::cout << "roll?\n";
    string YN;
    std::cin >> YN;
    while((YN == "Y") || (YN == "y"))
    {
        int i = 0;
        i++;
        srand(time((NULL)));
        std::cout << D1() << " " << D2() << " " << D3() << " " << D4() << " " << D5() << "\n";
        std::cout << "roll?\n";
        std::cin >> YN;
    }
}

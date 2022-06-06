#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <list>
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

int Ace()
{
    int AceCount = 0;
    if(D1() == 1)
    {
        AceCount++;
    }
    if(D2() == 1)
    {
        AceCount++;
    }
    if(D3() == 1)
    {
        AceCount++;
    }
    if(D4() == 1)
    {
        AceCount++;
    }
    if(D5() == 1)
    {
        AceCount++;
    }
    return AceCount;
}

int Twos()
{
    int TwoCount;
    if(D1() == 2)
    {
        TwoCount++;
    }
    if(D2() == 2)
    {
        TwoCount++;
    }
    if(D3() == 2)
    {
        TwoCount++;
    }
    if(D4() == 2)
    {
        TwoCount++;
    }
    if(D5() == 2)
    {
        TwoCount++;
    }
    return TwoCount;
}

int Threes()
{
    int ThreeCount;
    if(D1() == 3)
    {
        ThreeCount++;
    }
    if(D2() == 3)
    {
        ThreeCount++;
    }
    if(D3() == 3)
    {
        ThreeCount++;
    }
    if(D4() == 3)
    {
        ThreeCount++;
    }
    if(D5() == 3)
    {
        ThreeCount++;
    }
    return ThreeCount;
}
int Fours()
{
    int FourCount;
    if(D1() == 4)
    {
        FourCount++;
    }
    if(D2() == 4)
    {
        FourCount++;
    }
    if(D3() == 4)
    {
        FourCount++;
    }
    if(D4() == 4)
    {
        FourCount++;
    }
    if(D5() == 4)
    {
        FourCount++;
    }
    return FourCount;
}
int Fives()
{
    int FiveCount;
    if(D1() == 5)
    {
        FiveCount++;
    }
    if(D2() == 5)
    {
        FiveCount++;
    }
    if(D3() == 5)
    {
        FiveCount++;
    }
    if(D4() == 5)
    {
        FiveCount++;
    }
    if(D5() == 5)
    {
        FiveCount++;
    }
    return FiveCount;
}
int Sixs()
{
    int SixCount;
    if(D1() == 6)
    {
        SixCount++;
    }
    if(D2() == 6)
    {
        SixCount++;
    }
    if(D3() == 6)
    {
        SixCount++;
    }
    if(D4() == 6)
    {
        SixCount++;
    }
    if(D5() == 6)
    {
        SixCount++;
    }
    return SixCount;
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

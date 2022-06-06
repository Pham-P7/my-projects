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

void main()
{
    std::cout << "roll?\n";
    string YN;
    std::cin >> YN;
    while((YN == "Y") || (YN == "y"))
    {
        srand(time((NULL)));
        std::cout << D1() << " " << D2() << " " << D3() << " " << D4() << " " << D5() << "\n";
        int arr[] = {D1(),D2(),D3(),D4(),D5()};

        int OneCount = 0;
        for(int i = 0; i < 5; i++)
        {
            if(arr[i] == 1)
            {
                OneCount += 1;
            }
        }
        int TwoCount = 0;
        for(int i = 0; i < 5; i++)
        {
            if(arr[i] == 2)
            {
                TwoCount += 2;
            }
        }
        int ThreeCount = 0;
        for(int i = 0; i < 5; i++)
        {
            if(arr[i] == 3)
            {
                ThreeCount += 3;
            }
        }
        int FourCount = 0;
        for(int i = 0; i < 5; i++)
        {
            if(arr[i] == 4)
            {
                FourCount += 4;
            }
        }
        int FiveCount = 0;
        for(int i = 0; i < 5; i++)
        {
            if(arr[i] == 5)
            {
                FiveCount += 5;
            }
        }
        int SixCount = 0;
        for(int i = 0; i < 5; i++)
        {
            if(arr[i] == 6)
            {
                SixCount = SixCount + 6;
            }
        }
        std::cout << "roll?\n";
        std::cin >> YN;
    }
}

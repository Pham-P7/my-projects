#include <iostream>
#include <ctime>
void main()
{
    srand(time(NULL));
    int firstRoll = rand() % 10 + 1;
    while(true)
    {
        char station[] = "groundWater";
        if(firstRoll == 1 || station == "groundWater")
        {
            std::cout << "testing";
        }
    }
}
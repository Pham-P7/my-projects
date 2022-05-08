#include <iostream>
#include <string>
using namespace std;

int main()
{
    //equals-equals if trevor is smart that day
    if(1 == 1)
    {
        std::cout << "\nEquals\n";
    }
    //less
    if(1 - 1 <= 1)
    {
        std::cout << "Equals less\n";
    }
    //more
    if(1 + 1 >= 1)
    {
        std::cout << "Equals More\n";
    }
    //and 
    if((1 + 1 == 2) && (2 + 2 == 4))
    {
        std::cout << "And\n";
    }
    //or 
    if((1 + 1 == 3) || (2 + 2 == 4))
    {
        std::cout << "Or\n";
    }
    //not
    if(!(1 + 1 == 3))
    {
        std::cout << "Not\n";
    }

}
#include <iostream>
#include <cmath> 
#include <string>
using namespace std;

int main()
{
    //equals-equals if trevor is smart that day
    if(1 == 1)
    {
        std::cout << "Equals";
    }
    //less
    if(1 - 1 < 1)
    {
        std::cout << "Equals less";
    }
    //more
    if(1 + 1 > 1)
    {
        std::cout << "Equals Plus";
    }
    //and 
    if((1 + 1 == 2) && (2 + 2 == 4))
    {
        std::cout << "And";
    }
    //or 
    if((1 + 1 == 3) || (2 + 2 == 4))
    {
        std::cout << "Or";
    }
    //not
    if(!(1 + 1 == 3))
    {
        std::cout << "Not";
    }

}
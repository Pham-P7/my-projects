#include <iostream>
#include <string>
using namespace std;

int main()
{
    int i = 0;
    while(true)
    {
        i++;
        std::cout << i << "\n";
        if(i == 100)
        {
            break;
        }
    }
    return 0;
}
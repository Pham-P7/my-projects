#include<iostream>
using namespace std;

int Factorial(){
    int fac = 1;
    int x;
    std::cout << "What number would you like to factor?\n";
    std::cin >> x;
    if(x == 1)
    return fac;
    else
    {
        for(int i = 1; i <= x; i++)
        {
            fac = fac * i;
        }
        return fac;
    }
}
void main(){
    int y = Factorial();
    std::cout << "the factorial of your number is " << y;
}
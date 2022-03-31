#include <iostream>
int main()
{
    std::cout << "You have a long quest ahead and you must pack food, water and supplies";
    std::cout << std::endl;
    std::cout << "You must bring the EXACT AMOUNT or it will be to heavy or you will die";

    const int a = 4;
    const int b = 3;
    const int c = 7;

    const int sum = a + b + c;
    const int product = a * b * c;
    
    std::cout << std::endl;
    std::cout << sum << std::endl;
    std::cout << product << std::endl;

    return 0;
}
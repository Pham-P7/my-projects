#include <iostream>
int main()
{
    // main story 
    std::cout << "You have a long quest ahead and you must pack food, water and supplies";
    std::cout << std::endl;
    std::cout << "You must bring the EXACT AMOUNT or it will be to heavy or you will die";

    const int CodeA = 4;
    const int CodeB = 3;
    const int CodeC = 7;

    const int sum = CodeA + CodeB + CodeC;
    const int product = CodeA * CodeB * CodeC;
    
    std::cout << std::endl;
    std::cout << "There are 3 numbers in the password" << std::endl;
    std::cout << "The sum of all 3 numbers = " << sum << std::endl;
    std::cout << "The product of all 3 numbers = " << product << std::endl;

    return 0;
}
#include <iostream>

void PrintIntroduction()
{
    // main story 
    std::cout << "You have a long quest ahead and you must pack food, water and supplies \n";
    std::cout << "You must bring the EXACT AMOUNT or it will be to heavy or you will die \n";
}

void PlayGame()
{
    const int CodeA = 2;
    const int CodeB = 4;
    const int CodeC = 7;
    
    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;
    
    std::cout << "There are 3 numbers in the password";
    std::cout << "\n The sum of all 3 numbers = " << CodeSum;
    std::cout << "\n The product of all 3 numbers = " << CodeProduct << "\n";

    int GuessA, GuessB, GuessC;
    std::cin >> GuessA >> GuessB >> GuessC;

    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProuct = GuessA * GuessB * GuessC;
    
    if(GuessSum == CodeSum && GuessProuct == CodeProduct)
    {
        std::cout << "\nyou won!";
    }
    else
    {
        std::cout << "\nyou lose";
    }
}

int main()
{
    PrintIntroduction();
    PlayGame();
    return 0;
}

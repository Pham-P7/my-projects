#include <iostream>
#include <ctime>

void PrintIntroduction(int Difficulty)
{
    // output a line that tells what level you are on 

}

bool PlayGame(int Difficulty)
{
    PrintIntroduction(Difficulty);
    // difficulty rating 
    const int CodeA = rand() % (Difficulty + 2) + Difficulty;
    const int CodeB = rand() % (Difficulty + 2) + Difficulty;
    const int CodeC = rand() % (Difficulty + 2) + Difficulty;
    // create the sum of the product 
    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;
    //print the sum of the 3 numbers and the product of the 3 numbers
    std::cout << "\nThere are 3 numbers in the combination";


    // create the input guesses 


    // create the guess sum and product to compaire to code sum and product 


    
    if()
    {

    }
    else
    {

    }
}

int main()
{
    // time sets difficulty rating 
    srand(time(NULL));
    int LevelDifficulty = ;
    const int MaxLevel = ;
    // while level is less then max
    while ()
    {
        bool bLevelComplete = PlayGame(LevelDifficulty);
        std::cin.clear();
        std::cin.ignore();

        if ()
        {
            ++ LevelDifficulty;
        }
    }
    std::cout << "\nWell done";
    return 0;
}
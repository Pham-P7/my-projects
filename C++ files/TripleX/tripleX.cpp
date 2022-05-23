#include <iostream>
#include <ctime>

void PrintIntroduction(int Difficulty)
{
    // main story 
    std::cout << "\n\nYou are on level " << ("%i \n", Difficulty);
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
    //print the hints in the game
    std::cout << "\nThere are 3 numbers in the combination";
    std::cout << "\n The sum of all 3 numbers = " << CodeSum;
    std::cout << "\n The product of all 3 numbers = " << CodeProduct << "\n";
    // create the input guesses 
    int GuessA, GuessB, GuessC;
    std::cin >> GuessA >> GuessB >> GuessC;
    // create the guess sum and product to compaire to code sum and product 
    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProuct = GuessA * GuessB * GuessC;
    
    if(GuessSum == CodeSum && GuessProuct == CodeProduct)
    {
        std::cout << "\nyour correct";
        return true;
    }
    else
    {
        std::cout << "\nyou failed";
        return false;
    }
}

int main()
{
    // time sets difficulty rating 
    srand(time(NULL));
    int LevelDifficulty = 1;
    const int MaxLevel = 7;
    while (LevelDifficulty <= MaxLevel)
    {
        bool bLevelComplete = PlayGame(LevelDifficulty);

        if (bLevelComplete)
        {
            ++ LevelDifficulty;
        }
    }
    std::cout << "\nWell done";
    return 0;
}
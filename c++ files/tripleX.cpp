#include <iostream>
#include <ctime>

void PrintIntroduction(int Difficulty)
{
    // main story 
    std::cout << "\n\nYou have a long level " << Difficulty << " quest ahead and you must pack food, water and supplies\n";
    std::cout << "You must bring the EXACT AMOUNT or it will be to heavy or you will die \n";
}

bool PlayGame(int Difficulty)
{
    PrintIntroduction(Difficulty);
    const int CodeA = rand() % Difficulty + Difficulty;
    const int CodeB = rand() % Difficulty + Difficulty;
    const int CodeC = rand() % Difficulty + Difficulty;
    
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
        std::cout << "\nyou brought enough supplies for the whole quest";
        return true;
    }
    else
    {
        std::cout << "\nyou died due to lack of prep";
        return false;
    }
}

int main()
{
    srand(time(NULL));
    int LevelDifficulty = 1;
    const int MaxLevel = 7;
    while (LevelDifficulty <= MaxLevel)
    {
        bool bLevelComplete = PlayGame(LevelDifficulty);
        std::cin.clear();
        std::cin.ignore();

        if (bLevelComplete)
        {
            ++ LevelDifficulty;
        }
        

    }
    std::cout << "\nWell done, The guilds quest  board is currently empty congrats";
    return 0;
}
// Fill out your copyright notice in the Description page of Project Settings.
#include "BullCowCartridge.h"

void UBullCowCartridge::BeginPlay() // When the game starts
{
    Super::BeginPlay();
    SetupGame();
    PrintLine(FString::Printf(TEXT("The hiddenword is: %s. \n It is %i characters long"), *HiddenWord, HiddenWord.Len()));
    // or
    // PrintLine(TEXT("The hiddenword is: %s"), *HiddenWord);



    // set lives
}

void UBullCowCartridge::OnInput(const FString& Input) // When the player hits enter
{
    if(bGameOver)
    {
        ClearScreen();
        SetupGame();
    }
    else
    {
        ProcessGuess(Input);

    }
}

void UBullCowCartridge::SetupGame()
{    
    HiddenWord = TEXT("cake");
    int32 Lives = HiddenWord.Len();
    bGameOver = false;
    
    PrintLine(TEXT("Welcome to the Bulls and Cows game!"));
    PrintLine(TEXT("guess the %i letter word!"), HiddenWord.Len()); // remove the number later
    PrintLine(TEXT("you have %i lives", Lives));
    PrintLine(TEXT("type in your guess and press enter to continue"));
    IsIsogram(HiddenWord);
}
void UBullCowCartridge::EndGame()
{
    bGameOver = true;
    PrintLine(TEXT("\npress enter to play again"));
}
void UBullCowCartridge::ProcessGuess(FString Guess)
{
    if(Guess == HiddenWord)
    {
        PrintLine(TEXT("You have won!"));
        EndGame();
        return;
    }
        // check if isogram
    if(HiddenWord.Len() != Guess.Len())
    {
        PrintLine(TEXT("remember the hidden word has %i characters"), HiddenWord.Len());
        PrintLine(TEXT("sorry try guessing again, you have %i lives left"), lives);
        return;
    }
    if(!IsIsogram(Guess))
    {
        PrintLine(TEXT("no repeating letters, Guess again."));
        return;
    }
    --lives;
    PrintLine(TEXT("you have lost a life"));
    if(lives <= 0)
    {
        ClearScreen();
        PrintLine(TEXT("you have no lives left"));
        PrintLine(TEXT("the hidden word was %s"), *HiddenWord);
        EndGame();
        return;
    }
    PrintLine(TEXT("guess again, you still have %i lives left"), lives);
}
bool UBullCowCartridge::IsIsogram(FString Word)
{
    for (int32 Index = 0; Index < Word.Len(); Index++)
    {
        PrintLine(TEXT("%c", Word[Index]));
    }
    return true;
}
    // check if they want to play again
    // if yes start again
    // if no show word and quit game

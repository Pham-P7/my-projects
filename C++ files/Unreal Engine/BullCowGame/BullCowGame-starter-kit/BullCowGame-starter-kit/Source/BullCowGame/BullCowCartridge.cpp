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
    ClearScreen();

    HiddenWord.Len();
    Input.Len();

    if(Input == HiddenWord)
    {
        PrintLine(TEXT("You have won!"));
    }
    else
    {
        if(HiddenWord.Len() != Input.Len())
        {
            PrintLine(TEXT("opps the word is %i characters long, try again"), HiddenWord.Len());
        }

        PrintLine(TEXT("You lost"));
        bGameOver = true;
    }
    // check if isogram
    //check if right amount of characters 
    // remove life

    // check if they want to play again
    // if yes start again
    // if no show word and quit game
}

void UBullCowCartridge::SetupGame()
{    
    HiddenWord = TEXT("cake");
    bGameOver = false;
    
    PrintLine(TEXT("Welcome to the Bulls and Cows game!"));
    PrintLine(TEXT("guess the %i letter word!"), HiddenWord.Len()); // remove the number later
    PrintLine(TEXT("type in your guess and press enter to continue"));

    lives = 4;
    bGameOver = false;
}
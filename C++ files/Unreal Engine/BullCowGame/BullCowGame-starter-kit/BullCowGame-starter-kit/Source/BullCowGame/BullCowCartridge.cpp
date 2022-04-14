// Fill out your copyright notice in the Description page of Project Settings.
#include "BullCowCartridge.h"

void UBullCowCartridge::BeginPlay() // When the game starts
{
    Super::BeginPlay();
    PrintLine(TEXT("Welcome to the Bulls and Cows game!"));
    PrintLine(TEXT("guess the four letter word!")); // remove the number later
    PrintLine(TEXT("Press enter to continue"));
    HiddenWord = TEXT("cake");
}

void UBullCowCartridge::OnInput(const FString& Input) // When the player hits enter
{
    ClearScreen();
    PrintLine(Input);
    if(Input == HiddenWord)
    {
        PrintLine(TEXT("You have won!"));
    }
    else
    {
        PrintLine(TEXT("You have lose"));
    }
}
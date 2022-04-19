// Fill out your copyright notice in the Description page of Project Settings.
#include "BullCowCartridge.h"
#include "Misc/FileHelper.h"
#include "Misc/Paths.h"
void UBullCowCartridge::BeginPlay() // When the game starts
{
    const FString WordListPath = FPaths::ProjectContentDir() / TEXT("WordLists/HiddenWordList.txt");
    FFileHelper::LoadFileToStringArray(Words, *WordListPath);
    Super::BeginPlay();
    Isograms = GetValidWords(Words);
    SetupGame();
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
    HiddenWord = Isograms[FMath::RandRange(0, Isograms.Num() - 1)];
    int32 Lives = HiddenWord.Len();
    bGameOver = false;
    
    PrintLine(TEXT("Welcome to the Bulls and Cows game!"));
    PrintLine(TEXT("guess the %i letter word!"), HiddenWord.Len()); // remove the number later
    PrintLine(TEXT("you have %i lives"), Lives);
    PrintLine(TEXT("type in your guess and press enter to continue"));
    PrintLine(FString::Printf(TEXT("The hiddenword is: %s. \n It is %i characters long"), *HiddenWord, HiddenWord.Len()));
    // or
    // PrintLine(TEXT("The hiddenword is: %s"), *HiddenWord);
}
void UBullCowCartridge::EndGame()
{
    bGameOver = true;
    PrintLine(TEXT("\npress enter to play again"));
}
void UBullCowCartridge::ProcessGuess(const FString& Guess)
{
    if(Guess == HiddenWord)
    {
        PrintLine(TEXT("You have won!"));
        EndGame();
        return;
    }
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
bool UBullCowCartridge::IsIsogram(const FString& Word) const 
{
    for(int32 Index = 0; Index < Word.Len(); Index++)
    {
        for(int32 Comparison = Index + 1; Comparison < Word.Len(); Comparison++)
        {
            if(Word[Index] == Word[Comparison])
            {
                return false;
            }
        }
    }
    return true;
}
TArray<FString> UBullCowCartridge::GetValidWords(const TArray<FString>& WordList) const
{
    TArray<FString> ValidWords;
    for(FString Word : WordList)
    {
        if(Word.Len() >= 4 && Word.Len() <= 8 && IsIsogram(Word))
        {
            ValidWords.Emplace(Word);
        }
    }
    return ValidWords;
}

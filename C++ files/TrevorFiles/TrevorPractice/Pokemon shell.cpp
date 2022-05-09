/*
pokemon shell for Trevor
created by Phat Pham
*/
#include <iostream>
#include <string>
using namespace std;
void Introduction()
{
    string Name;
    std::cout << "what is your name?\n";
    std::cin >> Name;
    std::cout << ("\nHello %s, welcome to the world of pokemon\nThis however is a copy of the game so you get stuck with one battle\n", Name);
}
int PickPokemon()
{
    std::cout << "what will your first pokemon be?\n" << "(a) Charmander, (b) squrt gun, or (c) usless plant thing";
    char FirstPick;
    std::cin >> FirstPick;
}
bool Battle()
{

}
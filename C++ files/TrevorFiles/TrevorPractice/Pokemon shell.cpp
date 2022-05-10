/*
pokemon shell for Trevor
created by Phat Pham
*/
#include <iostream>
#include <string>
#include <fstream>
using namespace std;


class Pokemon
{
    public:
    string name, type;
    int attack, health, armor;
};
class Attack
{
    public:
    int attackMult, attackPlus;
    string statEffect;
};
void Introduction()
{
    string Name;
    std::cout << "what is your name?\n";
    std::cin >> Name;
    std::cout << ("\nHello %s, welcome to the world of pokemon\n",Name);
    std::cout << "This is a bad copy of pokemon made in a few hours so don't expect much";
}
int PickPokemon()
{

}
bool Battle()
{

}
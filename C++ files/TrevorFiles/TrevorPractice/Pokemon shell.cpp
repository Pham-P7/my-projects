/*
pokemon shell for Trevor
created by Phat Pham
*/
#include <iostream>
#include <string>
using namespace std;
class Pokemon
{
    public:
    string name;
    string type;
    int attack;
    int health;
    int armor;    
};
class Attack
{
    public:
    int damage;
};
void Introduction()
{
    string Name;
    std::cout << "what is your name?\n";
    std::cin >> Name;
    std::cout << ("\nHello %s, welcome to the world of pokemon\nThis however is a copy of the game made in a few hours so don't expect much\n", Name);
}
int PickPokemon()
{

}
bool Battle()
{

}
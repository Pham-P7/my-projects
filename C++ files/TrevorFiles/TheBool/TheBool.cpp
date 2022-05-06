#include <iostream>
int main()
{
    int answer;
    std::cout << "Please enter your answer for the following equation\n what is 1 + 1? \n ";
    std::cin >> answer; 
    if(1 + 1 == answer)
    {
        std::cout << "correct";
    }
    else
    {
        std::cout << "wrong";
    }
}
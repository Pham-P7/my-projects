#include <iostream>
#include <string>
using namespace std;
int main()
{
    int answer;
    std::cout << "Please enter your answer for the following equation\n what is 1 + 1? \n ";
    std::cin >> answer; 
    if(1 + 1 == answer)
    {
        string result = "correct";
        std::cout << result;
    }
    else
    {
        string result = "wrong";
        std::cout << result;
    }
}
// header statments 
#include <iostream>
#include <ctime>
#include <Windows.h>
#include <string>
using namespace std;
// main function sets off at 7 and keep keeps rechecking time 
int main()
{
    // start stopcode and ask for a variable
    string stopCode;
    std::cin >> stopCode; 
    while(true)
    {
        // checks the time until the
        time_t now = time(NULL);
        struct tm *tm_struct = localtime(&now);
        int hour = tm_struct->tm_hour;
        if(hour == 7 && stopCode != "go")
        {
            int c = 0;
            while(c != 1000 && stopCode != "go")
            {
                Beep(523,500);
                c++;
            }
        }
        return 0;
    }
}
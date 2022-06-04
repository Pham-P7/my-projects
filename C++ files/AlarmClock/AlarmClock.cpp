// header statments 
#include <iostream>
#include <ctime>
#include <Windows.h>
#include <string>
using namespace std;
// main function sets off at 7 and keep keeps rechecking time 
void main()
{
    // start stopcode and ask for a variable
    string stopCode;
    stopCode = "go";
    // starting waketime to reset later
    int WakeTime = 0;

    std::cout << "what time do you want to wake up? reminder please use military time:)\n";
    std::cin >> WakeTime;

    while(true)
    {
        // checks the time until the
        time_t now = time(NULL);
        struct tm *tm_struct = localtime(&now);
        int hour = tm_struct->tm_hour;
        // checks for current time to start 
        if(hour == WakeTime)
        {
            int c = 0;
            while(c != 1000)
            {
                Beep(523,500);
                c++;
            }
        }
    }
}
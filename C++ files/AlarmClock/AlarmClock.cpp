// this is my alarm clock because I can't get up in the morning
#include <iostream>
#include <ctime>
#include <windows.h>

int main()
{
    while(true)
    {
        time_t now = time(NULL);
        struct tm *tm_struct = localtime(&now);
        double hour = tm_struct->tm_hour;
        if(hour == 7)
        {
            int c = 0;
            while(c != 1000)
            {
                Beep(523,400);
                c++;
            }
        }
        return 0;
    }
}

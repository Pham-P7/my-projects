// this is my alarm clock because I can't get up in the morning
#include <iostream>
#include <ctime>

int main()
{
    while(true)
    {
        time_t now = time(NULL);
        struct tm *tm_struct = localtime(&now);
        double hour = tm_struct->tm_hour;
        if(hour == 7)
        {
            while(c != 1000 , c  = 0, c++)
            {
                Beep(523,500);
            }
        }
        return 0;
    }
}

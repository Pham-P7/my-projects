// this is my alarm clock because I can't get up in the morning
#include <iostream>
#include <ctime>
#include <Windows.h>

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
                Beep(523,500);
                c++;
                char stopCode[4];
                std::cin >> stopCode;
                if(stopCode == "stop")
                {
                    break;
                }
            }
        }
        return 0;
    }
}

/*
Phat Pham
Hello + Name
3/23/22
*/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hello___Name
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("enter your name: ");
            string Name = Console.ReadLine();
            Console.WriteLine("Hello " + Name);
            Console.WriteLine("Enter any key to exit");
            Console.ReadKey();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Echo_Echo
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

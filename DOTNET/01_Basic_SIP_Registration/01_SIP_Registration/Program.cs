using System;
using Ozeki.VoIP;
using Ozeki.VoIP.SDK;

namespace _01_SIP_Registration
{
    class Program
    {
        private static Softphone _mySoftphone;   // softphone object

        private static void Main(string[] args)
        {
            Console.WriteLine("This is a simple Ozeki VoIP SIP SDK demo written in C#.");
            Console.WriteLine("It can be used to register to a PBX by using SIP account.");
        }
    }
}

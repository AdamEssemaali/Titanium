using System;
using Titanium.Tokens;
using Titanium.Extensions;
class Program
{
    static void Main(string[] args)
    {

        foreach (var item in Enum.GetValues(typeof(Tokens)))
        {
            var value = Titanium.Extensions.EnumManagement.GetDescription((Enum)item);
            Console.WriteLine($"{ (object)value}:{ (object)item}");
        }
    }
}
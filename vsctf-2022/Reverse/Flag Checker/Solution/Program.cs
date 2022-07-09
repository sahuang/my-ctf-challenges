using System;
using System.Linq;

namespace VSCTF
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the flag: ");
            // vsctf{y0u_n33d_AES&BLOWFISH_727}
            string flag = Console.ReadLine();
            if (flag.Length != 32)
            {
                Console.WriteLine("Wrong flag.");
                return;
            }

            string s1 = flag.Substring(0, flag.Length / 2);
            string s2 = flag.Substring(flag.Length / 2);
            byte[] finale = Utils.OwO(s1).Concat(Utils.OaO(s2)).ToArray();

            if (finale.Length != 48)
            {
                Console.WriteLine("Wrong flag.");
                return;
            }

            for (int i = 0; i < finale.Length; ++i)
            {
                if ((Secrets.SuperConfidential[i] ^ i) != finale[i])
                {
                    Console.WriteLine("Wrong flag.");
                    return;
                }
            }

            Console.WriteLine("Correct! You got the flag.");
            return;
        }
    }
}

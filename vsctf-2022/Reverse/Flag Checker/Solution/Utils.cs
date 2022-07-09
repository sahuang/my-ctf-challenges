using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using BlowFish = Elskom.Generic.Libs.BlowFish;

namespace VSCTF
{
    class Utils
    {
        public static byte[] OwO(string input)
        {
            if (input == null || input.Length <= 0)
            {
                return Array.Empty<byte>();
            }

            byte[] encrypted;

            using (Aes custom = Aes.Create())
            {
                custom.Key = Encoding.ASCII.GetBytes(Secrets.rickroll);
                custom.IV = Encoding.ASCII.GetBytes(Secrets.dance);

                ICryptoTransform encryptor = custom.CreateEncryptor(custom.Key, custom.IV);

                using (MemoryStream msEncrypt = new MemoryStream())
                {
                    using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                    {
                        using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                        {
                            swEncrypt.Write(input);
                        }
                        encrypted = msEncrypt.ToArray();
                    }
                }
            }

            return encrypted;
        }

        public static byte[] OaO(string input)
        {
            if (input == null || input.Length <= 0)
            {
                return Array.Empty<byte>();
            }

            byte[] key = Encoding.ASCII.GetBytes(Secrets.fish);
            for (int i = 0; i < key.Length; ++i)
            {
                key[i] = (byte)(i ^ key[i]);
            }

            BlowFish bf = new BlowFish(key);
            bf.IV = Encoding.ASCII.GetBytes(Secrets.bite);
            return bf.EncryptCBC(Encoding.ASCII.GetBytes(input));
        }
    }
}

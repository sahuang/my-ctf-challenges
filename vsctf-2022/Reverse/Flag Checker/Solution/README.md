# Writeup

## Overview

We are given an executable, running it prompts user input and will print "Wrong flag" if the input isn't the flag. With some inspection we notice this is a c# program compiled executable, so we can use ILSpy to decompile.

Since nothing is stripped, we can easily see the 3 main files there. Let's check them one by one.

```cs
// VSCTF.Utils
using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using Elskom.Generic.Libs;
using VSCTF;

internal class Utils
{
	public static byte[] OwO(string input)
	{
		if (input == null || input.Length <= 0)
		{
			return Array.Empty<byte>();
		}
		using Aes aes = Aes.Create();
		aes.Key = Encoding.ASCII.GetBytes(Secrets.rickroll);
		aes.IV = Encoding.ASCII.GetBytes(Secrets.dance);
		ICryptoTransform transform = aes.CreateEncryptor(aes.Key, aes.IV);
		using MemoryStream memoryStream = new MemoryStream();
		using CryptoStream stream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
		using (StreamWriter streamWriter = new StreamWriter(stream))
		{
			streamWriter.Write(input);
		}
		return memoryStream.ToArray();
	}

	public static byte[] OaO(string input)
	{
		if (input == null || input.Length <= 0)
		{
			return Array.Empty<byte>();
		}
		byte[] bytes = Encoding.ASCII.GetBytes(Secrets.fish);
		for (int i = 0; i < bytes.Length; i++)
		{
			bytes[i] = (byte)(i ^ bytes[i]);
		}
		return new BlowFish(bytes)
		{
			IV = Encoding.ASCII.GetBytes(Secrets.bite)
		}.EncryptCBC(Encoding.ASCII.GetBytes(input));
	}
}
```

We have 2 functions in `Utils` class. Upon reading the code, we know `OwO` is taking a plain text as input and outputs AES encryoted cipher text (`using Aes aes = Aes.Create()`). Key and IV are all provided in the `Secrets` class. `OaO` is essentially a BlowFish encryption, however we had an extra step inside: Each byte is xor'd with its position index to get a new byte array as input to BlowFish.

```cs
// VSCTF.Program
using System;
using System.Linq;
using VSCTF;

internal class Program
{
	private static void Main(string[] args)
	{
		Console.Write("Enter the flag: ");
		string text = Console.ReadLine();
		if (text.Length != 32)
		{
			Console.WriteLine("Wrong flag.");
			return;
		}
		string input = text.Substring(0, text.Length / 2);
		byte[] array = Enumerable.Concat(second: Utils.OaO(text.Substring(text.Length / 2)), first: Utils.OwO(input)).ToArray();
		if (array.Length != 48)
		{
			Console.WriteLine("Wrong flag.");
			return;
		}
		for (int i = 0; i < array.Length; i++)
		{
			if ((Secrets.SuperConfidential[i] ^ i) != array[i])
			{
				Console.WriteLine("Wrong flag.");
				return;
			}
		}
		Console.WriteLine("Correct! You got the flag.");
	}
}
```

The program logic is simple:

1. Reads a string of length 32
2. Splits the string to 2 halves: first half is encrypted with AES, second half is encrypted with BlowFish
3. AES output + BlowFish output is a byte array of length 48, which will be compared against `Secrets.SuperConfidential[i] ^ i` to check the flag

To reverse engineer, we can either use Python to re-implement the algorithms or directly use C#. Let's try Python here. Note that AES encrypted plain text is a byte array of length 32, while BlowFish is 16 (summing up to 48).

Check exploit script for solving.
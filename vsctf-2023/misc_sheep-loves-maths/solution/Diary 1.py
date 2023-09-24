from oeis import *

print("Maths puzzles are fun.")

res = input("Enter the secret code: ")

assert len(res) == 8
assert ord(res[0]) in A000142[:10]
assert ord(res[1]) in A004767[:100] and ord(res[1]) > A000203[36]
assert ord(res[2]) == ord(res[0]) - 1
assert ord(res[3]) in A000045[:20]
assert ord(res[4]) == 2 * (ord(res[3]) + 1)
assert ord(res[5]) == ord(res[1]) - 1
assert ord(res[6]) in A000217[13:20]
assert ord(res[7]) == A000040[4] ** 2

print(f"I am going to keep my next diary at: https://challs.vsc.tf/sheep-diary-{res}/")

print("The Sheep,\nJun 1, 2022")
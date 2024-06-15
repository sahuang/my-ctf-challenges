#!/usr/local/bin/python
try:
    s = input("Submit the hash: ").strip().lower()
    if s == "b85478a2d0c66c43f395ab166a6a4aa07a39fdb08e097d23f1d057746887d37a":
        print("Congrats! Here's your flag: osu{Much_34s13r_Th4n_osu!Trivium_XD}")
    else:
        print("Nope!")
except:
    print("Unknown error occurred.")
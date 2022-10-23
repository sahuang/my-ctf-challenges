# Not Georainbolt

## Description

[Georainbolt](https://twitter.com/georainbolt) is able to guess the location on Google Map [in 0.1 seconds](https://www.tiktok.com/@georainbolt/video/7106684902929599786). Can you do it in a second?

Given an IP address or a coordinate, tell me which city it is in. All answers are case-insensitive. You will need a space between words, such as "new york city".

For simplicity, I will make it easy. There are 50 questions and you only need to achieve an accuracy of more than 50% to get the flag!

`nc 137.184.215.151 22606`

## Solution

There are many ways of solving the challenge.

- Use https://ip-api.com/docs/api:json to get the location of an IP address.
- Use http://api.positionstack.com to get the location from coordinates.

```py
from multiprocessing import context
from pwn import *
import requests

context.log_level = 'error'
io = remote("137.184.215.151", 22606)

for _ in range(50):
    io.recvuntil(b"/50. ")
    print(io.recvline().decode().strip())
    info = io.recvline().decode().strip()
    try:
        if "IP" in info:
            # Use https://ip-api.com/docs/api:json to get the location
            # GET http://ip-api.com/json/{ip}
            ip = info.split(" ")[-1]
            r = requests.get(f"http://ip-api.com/json/{ip}")
            if r.status_code == 200:
                city = r.json()["city"]
                city = city.lower()
                print("IP Guess:", city)
                io.recvuntil(b"City: ")
                io.sendline(city.lower().encode())
            else:
                io.recvuntil(b"City: ")
                io.sendline(b"shanghai")
        else:
            # example http://api.positionstack.com/v1/reverse?access_key=KEY&query=32.7157,-117.1647
            ll = info.split(":")[-1].strip().split(",")
            lat = ll[0].strip()
            lon = ll[1].strip()
            r = requests.get(f"http://api.positionstack.com/v1/reverse?access_key=REDACTED&query={lat},{lon}")
            if r.status_code == 200:
                city = r.json()["data"][0]["locality"]
                city = city.lower()
                print("Geo Guess:", city)
                io.recvuntil(b"City: ")
                io.sendline(city.lower().encode())
            else:
                io.recvuntil(b"City: ")
                io.sendline(b"shanghai")
    except:
        io.recvuntil(b"City: ")
        io.sendline(b"shanghai")

io.interactive()
```
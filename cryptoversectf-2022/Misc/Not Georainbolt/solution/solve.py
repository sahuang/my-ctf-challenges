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
            # example http://api.positionstack.com/v1/reverse?access_key=6de6ab97a433ccb8eda4a5179185435b&query=32.7157,-117.1647
            # info is like Coordinate (lat, lon): 51.5085, -0.1257
            ll = info.split(":")[-1].strip().split(",")
            lat = ll[0].strip()
            lon = ll[1].strip()
            r = requests.get(f"http://api.positionstack.com/v1/reverse?access_key=6de6ab97a433ccb8eda4a5179185435b&query={lat},{lon}")
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
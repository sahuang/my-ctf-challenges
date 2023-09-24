from pwn import *
from base64 import b64encode

data = open('fixed_model.h5', 'rb').read()

io = remote('172.86.96.174', 10105)
io.sendlineafter(b"model: ", b64encode(data))
io.interactive()
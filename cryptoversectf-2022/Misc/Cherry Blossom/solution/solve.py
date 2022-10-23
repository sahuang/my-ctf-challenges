from pwn import *
from tqdm import tqdm

# log level
context.log_level = 'error'

def calculate(blossom, n, m):
    assert len(blossom) == n
    res = 0
    curr = 0
    l, r = 0, 0
    # iterate blossom array, find the max subarray sum whose length is less or equal to m
    while r < n:
        curr += blossom[r]
        if curr < 0:
            l = r + 1
            r = l
            curr = 0
            continue
        res = max(res, curr)
        r += 1
        if r == n: break
        if r - l + 1 > m:
            curr -= blossom[l]
            l += 1
    return res

io = remote('137.184.215.151', 22602)

for _ in tqdm(range(10)):
    io.recvuntil(b'Input:\n')
    n, m = map(int, io.recvline().split())
    blossom = list(map(int, io.recvline().split()))
    io.recvuntil(b'Output: ')
    io.sendline(str(calculate(blossom, n, m)).encode())
io.interactive()
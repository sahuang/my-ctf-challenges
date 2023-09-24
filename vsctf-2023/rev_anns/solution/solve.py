from pwn import *
from ctypes import CDLL
import numpy as np
import faiss

io = remote('34.41.254.29', 3088)
libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
libc.srand(libc.time(0))

for _ in range(4): io.recvline()

def get_random(libc):
    return libc.rand() / 2147483647.0

d = 128
nb = 100000
nq = 10
nlist = 100
k = 3
nprobe = 10

xb = []
for i in range(nb):
    xb.append([get_random(libc) for _ in range(d)])
    xb[i][0] += i/1000.0
xb = np.array(xb).astype('float32')

quantizer = faiss.IndexFlatL2(d)
index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)

assert not index.is_trained
index.train(xb)
assert index.is_trained
index.add(xb)

xq = []
for i in range(nq):
    xq.append([get_random(libc) for j in range(d)])
    xq[i][0] += i/1000.0
xq = np.array(xq).astype('float32')

index.nprobe = nprobe
D, I = index.search(xq, k)
print(I)

for i in range(nq):
    target = str(int(I[i][0])) + " " + str(int(I[i][1])) + " " + str(int(I[i][2]))
    io.sendlineafter(b">", target.encode())
    print(io.recvline().decode())

io.interactive()
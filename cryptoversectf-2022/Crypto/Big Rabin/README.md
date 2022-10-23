# Big Rabin

## Description

Rabin cryptosystem, but big.

## Solution

Brute-force the possible plaintexts.

Note: Because `e` is small and `n` is too large, it turns out you can just sqrt `c` and get the plaintext. My bad on getting the unintended :(

```py
from Crypto.Util.number import *
from gmpy2 import *
from sympy.ntheory.modular import *
from sympy.ntheory.residue_ntheory import nthroot_mod

x = [] # truncated
c = # truncated
e = 2

y = []
for i in x:
    y.append(nthroot_mod(c,e,i))
    y.append(i - nthroot_mod(c,e,i))
yy = []

for i in range(1024):
    s = bin(i)[2:].rjust(10,'0')
    yyy = []
    for j in range(10):
        yyy.append(y[j*2+int(s[j])])
    yy.append(yyy)

for i in yy:
    m = long_to_bytes(crt(x,i)[0])
    if b'cvctf' in m:
        print(m[256:].decode())
```
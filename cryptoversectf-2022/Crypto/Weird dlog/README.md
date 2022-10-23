# Weird dlog

## Description

Can you decrypt this message?

## Solution

1. Since `p` and `q` are close, we can use Fermat's theorem to factorize `n` and find `p` and `q`.
2. Second part is [Okamoto–Uchiyama cryptosystem](https://en.wikipedia.org/wiki/Okamoto%E2%80%93Uchiyama_cryptosystem). Decrypt using its formula.

```py
from Crypto.Util.number import *
from gmpy2 import *

g = # g
n = # n
m = # m

n = mpz(n)
p = iroot(n, 3)[0]
if p % 2 == 0: p += 1

while n % p != 0:
    p += 2

assert n % p == 0
if n % (p**2) == 0:
    q = n // (p**2)
else:
    q = iroot(n // p, 2)[0]
    p, q = q, p
    
assert p**2 * q == n

a = (pow(m, p-1, p**2) - 1)//p
b = (pow(g, p-1, p**2) - 1)//p
b_ = pow(b, -1, p)
m = a * b_ % p

print(long_to_bytes(m).decode())
```
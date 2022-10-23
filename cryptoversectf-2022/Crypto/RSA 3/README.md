# RSA 3

## Description

Secrets are hidden under the randomness.

`nc 137.184.215.151 22629`

## Solution

Simple Hastad's Broadcast Attack. We can query server until receiving enough ciphertexts on `e=17`. 

The "randomness" happens with low probability, so we can actually query a bit more ciphertexts then do a subset to avoid the randomness.

Solve script referenced some code from crypto-attacks repo.

```py
from sage.all import crt, ZZ
from math import gcd
from pwn import *
from Crypto.Util.number import *
import random

# log level
context.log_level = 'error'

def lcm(a):
    if len(a) == 1:
        return a[0]
    return a[0] * lcm(a[1:]) // gcd(a[0], lcm(a[1:]))

def fast_crt(X, M, segment_size=8):
    """
    Uses a divide-and-conquer algorithm to compute the CRT remainder and least common multiple.
    :param X: the remainders
    :param M: the moduli (not necessarily coprime)
    :param segment_size: the minimum size of the segments (default: 8)
    :return: a tuple containing the remainder and the least common multiple
    """
    assert len(X) == len(M)
    assert len(X) > 0
    while len(X) > 1:
        X_ = []
        M_ = []
        for i in range(0, len(X), segment_size):
            if i == len(X) - 1:
                X_.append(X[i])
                M_.append(M[i])
            else:
                X_.append(crt(X[i:i + segment_size], M[i:i + segment_size]))
                M_.append(lcm(M[i:i + segment_size]))
        X = X_
        M = M_

    return X[0], M[0]

def attack(e, c):
    """
    Recovers the plaintext from a ciphertext, encrypted using a very small public exponent (e.g. e = 3).
    :param e: the public exponent
    :param c: the ciphertext
    :return: the plaintext
    """
    return int(ZZ(c).nth_root(e))

def hastad(N, e, c):
    """
    Recovers the plaintext from e ciphertexts, encrypted using different moduli and the same public exponent.
    :param N: the moduli
    :param e: the public exponent
    :param c: the ciphertexts
    :return: the plaintext
    """
    assert e == len(N) == len(c), "The amount of ciphertexts should be equal to e."

    for i in range(len(N)):
        for j in range(len(N)):
            if i != j and gcd(N[i], N[j]) != 1:
                raise ValueError(f"Modulus {i} and {j} share factors, Hastad's attack is impossible.")

    c, _ = fast_crt(c, N)
    return attack(e, c)

e = 17
N = []
ct = []
while len(N) < 30:
    io = remote("137.184.215.151", 22629)
    io.recvuntil(b"n = ")
    n = int(io.recvline().strip())
    io.recvuntil(b"e = ")
    e = int(io.recvline().strip())
    if e != 17:
        io.close()
        continue
    io.recvuntil(b"c = ")
    c = int(io.recvline().strip())
    io.close()
    N.append(n)
    ct.append(c)
    print(f"{len(N)} / 30")

# Because some ct are randomly changed (with a chance of 10%), we need to randomly query N/ct
# Choose random 17 indices from N and ct
while True:
    indices = random.sample(range(len(N)), 17)
    N_curr = [N[i] for i in indices]
    ct_curr = [ct[i] for i in indices]
    try:
        pt = hastad(N_curr, e, ct_curr)
    except:
        continue
    if "cvctf" in long_to_bytes(pt).decode():
        print(long_to_bytes(pt).decode())
        break
```
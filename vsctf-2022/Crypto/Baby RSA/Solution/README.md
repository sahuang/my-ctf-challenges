# Baby RSA

## Solution

We are given `pubkey.pem`, from which we could retrieve `n` and `e`. Since `p` and `q` are only 128-bit primes, we can use tools like `yafu` to easily factorize `n`.

The only issue here is that `p-1` and `q-1` are not coprime with `e`, so `d*e = 1 (mod phi(n))` is not valid. This can be solved by using `nth_root()` in sage to first find all roots of `p` and `q`, then apply `crt` to all possible pairs. DiceCTF's [baby-rsa](https://ctftime.org/writeup/32264) script can be directly modified and used.

```py
from Crypto.Util.number import *
from Crypto.PublicKey import RSA

with open("pubkey.pem", "r") as f:
    key = RSA.importKey(f.read())
    e, n = int(key.e), int(key.n)

# yafu
p = 184980129074643957218827272858529362113
q = 283378097758180413812138939650885549231
c = 0x459cc234f24a2fb115ff10e272130048d996f5b562964ee6138442a4429af847

assert p * q == n

p_roots = mod(c, p).nth_root(e, all=True)
q_roots = mod(c, q).nth_root(e, all=True)

for xp in p_roots:
    for xq in q_roots:
        x = crt([Integer(xp), Integer(xq)], [p,q])
        x = int(x)
        flag = long_to_bytes(x)
        if flag.startswith(b"vsctf"):
            print(flag.decode())
            # vsctf{5m411_Pr1m3_15_Un54f3!}
```
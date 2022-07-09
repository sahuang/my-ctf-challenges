# Baby RSA

## Solution

Key function to analyze:

```py
def getStrongestPrime(nbits):
	while True:
		p = getStrongPrime(nbits)
		delta = random.randint(0x1337, 0x1337 + 0x1337)
		pp = p - delta
		ppp = prevprime(factorial(pp) % p)
		if gcd(ppp-1, e) == 1:
			return p, ppp
```

We are given `p` and we want to figure out `ppp`. Therefore we need to know `factorial(pp) % p`. Notice that `(p-1)! % p = -1` from Wilson's Theorem. Hence `(p-1)*(p-2)*...*(p-delta+1)*factorial(p-delta) % p = -1`.

We can brute force all `delta`, get `res = (p-1)*(p-2)*...*(p-delta+1) % p`, then `factorial(p-delta) % p = invert(-1 * res)`.

```py
from Crypto.Util.number import *
from sympy import *
from gmpy2 import *
from math import gcd
import random

p0 = [...]
q0 = [...]
N = [...]
e = 65537
c = [...]

def getStrongestPrime(nbits):
	while True:
		p = getStrongPrime(nbits)
		delta = random.randint(0x1337, 0x1337 + 0x1337)
		pp = p - delta
		ppp = prevprime(factorial(pp) % p)
		if gcd(ppp-1, e) == 1:
			return p, ppp

def recoverPrime(A, B):
	ans = 1
	for i in range(B + 1, A):
		ans=(i * ans) % A
	ans = -1 * ans
	s=invert(ans,A)
	return prevprime(s)

# brute force delta to get a factor of N. We use q0 which is faster
from tqdm import tqdm
for i in tqdm(range(0x1337, 0x1337 + 0x1337 + 1)):
	B = q0 - i
	tmp = recoverPrime(q0, B)
	if N % tmp == 0:
		real_p = tmp
		break

assert N % real_p == 0
real_q = N // real_p
phi = (real_p - 1) * (real_q - 1)
d = inverse(e, phi)
print(long_to_bytes(pow(c,d,N)).decode()) # vsctf{Strongest_can_be_the_weakest:(}
```
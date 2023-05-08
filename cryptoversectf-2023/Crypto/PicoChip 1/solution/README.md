# Writeup

## Intro

This challenge was made while reading some paper about RSA side channel attack. Due to lack of hardware devices, I tried to simulate it in Python so it is just a simplified version of the original challenge. Meant for people without any side channel analysis experience to solve as well. Here's the paper: [A New Side-Channel Attack on RSA Prime Generation](https://www.iacr.org/archive/ches2009/57470141/57470141.pdf).

## Solution

Paper has the attack listed. Upon inspecting the code, we see PicoChip first generates 60 odd primes in ascending order, then generates `p`, `q` primes by applying simple division on the primes. A random `k`-bit odd number is first generated and then we add 2 to it if it fails prime division or subsequent Miller-Rabin test. Signals are in the end plotted on interacted graph.

From paper,

> Power analysis allows a potential attacker to identify for each prime candidate v after which trial division the while-loop in Step 2b terminates. Moreover, he is able to realize whether Miller-Rabin primality test(s) have been performed.

The basic attack is explained in section 3.1 so I will not explain too much. Basically from the place where signal 0 is received we know some modular expression about `p` or `q`. In the end apply CRT to it. The formula given:

We assume that the candidate `vm := v0 + 2m` is prime, i.e. `p = vm`. If for `vj = v0 + 2j` signal 0 is received after the trial division by `ri` then `vj` is divisible by `ri`. This gives `p = vj + 2(m − j) ≡ 2(m − j) (mod ri)`. 

## Get flag

First of all we open `power_states.html` and record the signal values.

```py
power = [66, 0, 10, 0, 0, 1, 0, 60, 0, 0, 2, 0, 3, 0, 0, 17, 0, 60, 0, 0, 12, 0, 1, 0, 0, 4, 0, 41, 0, 0, 1, 0, 6, 0, 0, 65, 0, 0, 2, 0, 1, 0, 0, 3, 0, 48, 0, 0, 1, 0, 2, 0, 0, 29, 0, 28, 0, 0, 60, 0, 5, 0, 0, 16, 0, 1, 0, 0, 25, 0, 61]
```

We first figure out where does `p` prime generation end and `q` starts. Since for `p` to be prime, we need 60 prime checks + 1 Miller-Rabin test, the number of signal 1 (`State.SUCCESS`) must be >= 61. This means the 65 in middle is the place. Therefore `m = 21`. (Count number of 0's between start and 65.)

So now, from this array, we can infer the following in order:

- `power[0] = 66`: First 60 are for prime list generation. Then 6 numbers are analysed before current number `v0` is divisible by some prime. The prime is then 7th in list, or 19.
- `power[1] = 0`: `v0` is divisible by 19, or `p % 19 == 2 * (21 - 0) % 19 == 4`.
- `power[2] = 10`: `v0` is not divisible by 19, so we add 2 to it and try again. 10 numbers are analysed before current number `v1` is divisible by some prime. The prime is then 11th in list, or 37.
- `power[3] = 0`: `v1` is divisible by 37, or `p % 37 == 2 * (21 - 1) % 37 == 3`.

We do this until the end to obtain a list of `p % primes[i]`. Notice that if `power[j] == 60` it means all primes are checked and we move on to Miller-Rabin test. We can ignore this. Now we do a CRT over the numbers.

```py
from sage.all import *

'''
p % 2 == 1
p % 19 == 4
p % 37 == 3
p % 3 == 2
p % 5 == 1
p % 7 == 2
p % 11 == 6
p % 67 == 24
p % 43 == 18
p % 13 == 12
p % 191 == 10
'''
print(CRT_list([1,4,3,2,1,2,6,24,18,12,10], [2,19,37,3,5,7,11,67,43,13,191])) # 66491128391
```

We get `p = 66491128391`. Similarly we can get `q = 62337717991` with

```py
print(CRT_list([1,3,1,3,1,10,30,20,18,12,8], [2,13,3,7,5,11,229,127,113,17,61])) # 62337717991
```

Now we proceed to get flag.

```py
p = 66491128391
q = 62337717991
e = 0x10001
d = pow(e, -1, (p-1)*(q-1))
ct = 3059648962482294740345
print(long_to_bytes(pow(ct, d, p*q)).decode()) # p1C@-_
```

Flag is `cvctf{p1C@-_}`.
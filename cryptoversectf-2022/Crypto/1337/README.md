# 1337

## Description

A leet challenge.

## Solution

A challenge on basic Sage usage: `PolynomialRing`, `Ideal` and `variety` are very powerful. (I learned it from a past CTF and thought it's good to put in beginner CTFs.)

```py
a = [213929627434382339098735177055751649916, 19199104003461693263250446715340616788, 81305572597778258494448971196865605263, 204055349607012377951682156574173649079, 2268211308285612387872477045295901103]
p = 231609284865232306744388160907453774453

from Crypto.Util.number import long_to_bytes

P.<x,y,z,w> = PolynomialRing(FiniteField(p))
I = Ideal([x+y**3+z**3+w**7-a[0],y+z**3+w**3+x**7-a[1],z+w**3+x**3+y**7-a[2],w+x**3+y**3+z**7-a[3], x+y+z+w-a[4]])
ans = I.variety()

for _,v in ans[0].items():
    print(long_to_bytes(int(v)).decode(), end='')
```
# Writeup

This is a very simple challenge of `z3` and `rc4`. Challenge description has already hinted towards using `z3` to solve.

Loading the binary into IDA, the logic is clear: 

1) First check is on length - serial key is length 35.

2) Second check is on string format.

```cpp
for ( i = 0; i < strlen(a1); ++i )
{
    if ( i % 6 == 5 && a1[i] != 45 )
        return 0LL;
}
```

The string is in format `XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX`.

3) Third check can be solved with `z3` and it's based on sections 1,3,5 of serial key.

```py
from z3 import *

def all_smt(s, initial_terms):
	def block_term(s, m, t):
		s.add(t != m.eval(t))
	def fix_term(s, m, t):
		s.add(t == m.eval(t))
	def all_smt_rec(terms):
		if sat == s.check():
		   m = s.model()
		   yield m
		   for i in range(len(terms)):
			   s.push()
			   block_term(s, m, terms[i])
			   for j in range(i):
				   fix_term(s, m, terms[j])
			   yield from all_smt_rec(terms[i:])
			   s.pop()
	yield from all_smt_rec(list(initial_terms))

flag = [BitVec('f_'+str(i), 8) for i in range(35)]
s = Solver()

for i in range(35):
	if i % 6 == 5:
		s.add(flag[i] == ord('-'))
	elif i % 12 in [6,7,8,9,10]:
		s.add(flag[i] == ord('X'))
	else:
		s.add(Or(And(flag[i] >= 48, flag[i] <= 57), And(flag[i] >= 65, flag[i] <= 90)))
s.add(flag[0]+flag[2]+flag[4]+flag[13]+flag[15]+flag[24]+flag[26]+flag[28] == 486)
s.add(flag[0]*flag[1]-flag[4]+flag[12]*flag[13]-flag[16]+flag[24]*flag[25]-flag[28] == 13713)
s.add(flag[3]*flag[14]*flag[27]-flag[2]*flag[15]*flag[25] == -6256)
s.add((flag[1]-flag[3])*flag[4] == 48)
s.add(((flag[13]<<3)-(flag[15]<<2))*flag[14] == 20604)
s.add(((flag[28]<<2)-(flag[0]<<2))*flag[27] == -5616)
s.add(flag[4]-flag[3]-flag[2]-flag[1]+flag[0]*flag[0] == 6744)
s.add(flag[16]-flag[15]-flag[14]-flag[13]+flag[12]*flag[12] == 2405)
s.add(flag[28]-flag[27]-flag[26]-flag[25]+flag[24]*flag[24] == 4107)
s.add(flag[14] < 58)
s.add((flag[14]+flag[24])*(flag[28]-flag[1]) == -1508)

for m in all_smt(s, flag):
	flag_bytes = bytes([m.eval(flag[i]).as_long() for i in range(len(flag))])
	print(flag_bytes)
```

This gives `SE8D0-XXXXX-2K31P-XXXXX-AD648-XXXXX` as output which is what we want.

4) The final check is a bit tricky. As we can see from the binary, we have a key `vsCTF is a capture the flag competition organized by Team View Source. vsCTF is meant for players of all skill levels and everyone is welcomed to participate and learn.` stored in `v12`. We also have:

```cpp
for ( i = 0; i < strlen(s); ++i )
{
    if ( i % 12 > 5 && i % 12 <= 10 )
    {
        v4 = v6++;
        v23[v4] = s[i];
    }
}
```

This means the check is based on sections 2,4,6 of serial key. Here we copied the string of length 15 (5+5+5) to `v23`.

```c
sub_1774(v11, v12, v5);
sub_1A51(v11, v23, v9);
```

`sub_1774` takes the key and initialized `v11` based on some shifting, in fact `v11` is the sbox. `sub_1A51` did some xor to the data and if you have some knowledge of `rc4` you should notice it is `rc4` implementation. You do not need to reimplement the logic since there are already `rc4` python codes online to use.

The `rc4` crypt result is compared to some string `nRYEZjDuqxtlL8L6EatC` and we can probably notice it is base64 encoded. So we just write some code to decode string and decrypt rc4 to get the second part of serial key.

```py
from base64 import b64decode

# Copied rc4 implementation online
def rc4(data, key, skip=1024):
    x = 0
    box = list(range(256))

    x = 0
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        tmp = box[i]
        box[i] = box[x]
        box[x] = tmp

    x = 0
    y = 0
    out = []
    if skip > 0:
        for i in range(skip):
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
	
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        k = box[(box[x] + box[y]) % 256]
        # print(k)
        out.append(chr(char ^ k))

    return ''.join(out)


data = [x for x in b64decode("nRYEZjDuqxtlL8L6EatC")]
print(rc4(data, "vsCTF is a capture the flag competition organized by Team View Source. vsCTF is meant for players of all skill levels and everyone is welcomed to participate and learn.", 0))

# vsctf4beginnerz
```

Therefore our serial key is `SE8D0-vsctf-2K31P-4begi-AD648-nnerz`. Feeding it to server gives the flag `vsctf{you_are_good_at_z3,but_maybe_i_should_play_genshin_impact_first?}`.
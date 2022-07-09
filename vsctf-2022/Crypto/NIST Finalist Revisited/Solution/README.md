# NIST Finalist: Revisited

## Solution

The paper to refer to: [Collision Attacks on Round-Reduced Gimli-Hash/Ascon-Xof/Ascon-Hash](https://eprint.iacr.org/2019/1115.pdf)

In Section 5.1 it gave an example collision:

```
Table 11. A collision in 2-round Ascon-Xof with a 64-bit output
Message 1 05b93c0000000000fd000000fb
Message 2 05b93c0000000000fd000000db
Output 387fc9cc6fc5e428
```

If we run the messages locally we would indeed get a collision, but hash output is `7692b2e150b42b17` which is different from the paper. This is likely due to implementation modifications since we changed a few constants in `ascon.py` (`pyascon` only supports 32-byte hash output which is even worse).

It does not matter though - we can get our first collision with the example. But the second collision requires `m1` and `m2` to contain `admin` byte string. Some further reading of the paper: "The padded message pair need to satisfy ∆M1 = 0, ∆M2 = 0000000020000000".

We can try to get a collision by following the same pattern.

```py
def collision(m1: bytes, m2: bytes) -> bool:
    return ascon_xof(m1) == ascon_xof(m2)

m1 = b"admin" + b"\x00"*3
m2 = b"admin" + b"\x00"*3

for u in range(256):
    for b in range(220):
        tm1 = m1 + bytes([u]) + b"\x00"*3 + bytes([b])
        tm2 = m2 + bytes([u]) + b"\x00"*3 + bytes([b+0x20])
        if collision(tm1, tm2):
            print("collision:", bytes_to_hex(tm1), bytes_to_hex(tm2))
            exit(0)
```

There are a lot of collisions and we can take the first:

`collision: 61646d696e0000001000000008 61646d696e0000001000000028`

```bash
$ python3 ascon.py 
12 rounds of Ascon is surely collision resistant. What about 2-round Ascon?
If you can find two collisions for me, I will give you the flag!

1. Please send two hex encoded messages m1, m2 formatted in JSON:
{"m1":"05b93c0000000000fd000000fb", "m2":"05b93c0000000000fd000000db"}
Nice, collision found!

2. Please send another two hex encoded messages m1, m2 formatted in JSON:
{"m1":"61646d696e0000001000000008", "m2":"61646d696e0000001000000028"}
Nice, collision found again! Here is your flag: vsctf{REDACTED}
```

This is not really a challenge to "learn and implement" a paper - afterall this is a 24 hour beginner-friendly CTF. Player is expected to skim through the paper and find the relevant information, which is not too hard.

PS. I did not think of making this challenge until NIST announcement 3 days ago..
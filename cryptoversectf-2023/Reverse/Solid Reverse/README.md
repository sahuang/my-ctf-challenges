# Solid Reverse

Crypto in reverse??

## Solution

From the contract, we need to figure out the `key`, and `flag` is just xor of `key` and `goal`.

Check the key function:

```js
modifier checker(bytes16 key) {
    require(bytes8(key) == 0x3492800100670155, "Wrong key!");
    require(uint64(uint128(key)) == uint32(uint128(key)), "Wrong key!");
    require(magic1(uint128(key), 16) == 0x1964, "Wrong key!");
    require(magic2(uint64(uint128(key))) == 16, "Wrong key!");
    _;
}
```

In Solidity, when type casting `bytes16` to `bytes8`, it will only take the first 8 bytes. So we know the first 8 bytes of `key` is `0x3492800100670155`.

On the other hand, `uint` casting take the lower bits. Given `uint64` and `uint32` of cast are equal, we know the first 4 bytes of lower half of `key` is `0x00000000`.

Reading source code, we know `magic1(x, n)` will get the last `n` bits of `x`, so last 2 bytes of `key` is `0x1964`. We also know `magic2(x)` returns the index of the first `1` bit, because it is 16, we come to know `key[12:14] = 0x0001`. (`0x0000` will yield 15, and `0x0010` will yield 17.)

The whole key is `0x34928001006701550000000000011964`. We now know the flag: `0x34928001006701550000000000011964 ^ 0x57e4e375661c72654c31645f78455d19 = 0x63766374667b73304c31645f7844447d`, or `cvctf{s0L1d_xDD}`.
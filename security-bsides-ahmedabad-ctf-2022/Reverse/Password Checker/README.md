# Password Checker

## Difficulty
Easy

## Description
A rusty password checker... Maybe it is easy to break.

## Attachment
[password_checker](./checker)

## Solution

The binary is a simple password checker coded in Rust. It accepts flag input, does some arithmetic operations, then output is compared with a const array. The main logic can be found with decompiled code. Solve script attached below.

```py
res = [396, 870, 667, 761, 645, 866, 789, 545, 282, 629, 725, 282, 317, 726, 309, 317, 289, 796, 717, 267, 719, 395, 317, 407, 521, 426, 485, 822]
curr = 0x42

for i in range(len(res)):
    print(chr((res[i] ^ curr) // 7), end='')
    curr += 1
```
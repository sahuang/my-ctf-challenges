# My Online Voucher

## Description

Can you find the voucher code to redeem the free flag?

## Attachments

[chall](./chall)

## Solution

The source code is actually extremely simple. It checks product of ascii of neighboring characters in the input string. If the product array is equal to the const array given in the code, it will validate. Since we know `voucher[0] = 'c'`, we can get rest of the characters easily.

```c
int main(int argc, char **argv) {
    int i = 0;
    char voucher[20];
    int nums[19];

    printf("Enter voucher code: ");
    scanf("%20s", voucher);
    if (strlen(voucher) != 20) {
        printf("Invalid.\n");
        return 1;
    }

    nums[0] = 11682; nums[1] = 11682; nums[2] = 11484; nums[3] = 11832;
    nums[4] = 12546; nums[5] = 9471; nums[6] = 3696; nums[7] = 4128;
    nums[8] = 4386; nums[9] = 5049; nums[10] = 4752; nums[11] = 5280;
    nums[12] = 11220; nums[13] = 11934; nums[14] = 6201; nums[15] = 2597;
    nums[16] = 5390; nums[17] = 11330; nums[18] = 12875;

    // cvctf{M0V3c0nfu51ng}
    for (i = 0; i < 19; i++) {
        if (voucher[i] * voucher[i+1] != nums[i]) {
            printf("Invalid.\n");
            return 1;
        }
    }
    printf("Valid.\n");
    return 0;
}
```

The hard part, comes from the fact that the binary is not simply compiled with `gcc`. As the title hints, it is using [movfuscator](https://github.com/Battelle/movfuscator) to compile, which compiles programs into "mov" instructions, and only "mov" instructions.

You can use [demovfuscator](https://github.com/kirschju/demovfuscator) to translate the binary. Please note that this tool cannot magically convert the binary into a simple `gcc`-compiled binary which can be easily decompiled. The main goal is to recover the control flow of the original program from movfuscated binaries.

Once you have the control flow, because in the binary we will `return` once input is invalid in `for` loop, we can simply brute force each character by setting breakpoint and checking exit status.
// C89 compiler, don't use C99 features
#include <stdio.h>
#include <stdlib.h>

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
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include "rc4.h"
#include "zzz.h"

const char* BANNER =
"    __  __  __  __                             \n"
"   / / / /__\\ \\/ /___ _   _____  _____________ \n"
"  / /_/ / __ \\  / __ \\ | / / _ \\/ ___/ ___/ _ \\\n"
" / __  / /_/ / / /_/ / |/ /  __/ /  (__  )  __/\n"
"/_/ /_/\\____/_/\\____/|___/\\___/_/  /____/\\___/ \n"
"                                               \n";

void readFlag() {
    int c;
    FILE *file;
    file = fopen("flag", "r");
    if (file) {
        while ((c = getc(file)) != EOF)
            putchar(c);
        fclose(file);
        printf("\n");
    } else {
        printf("vsctf{go_to_server_for_the_real_flag!}\n");
    }
}

bool check1(const char* s) {
    for (int i = 0; i < strlen(s); i++) {
        if (i % 6 == 5) {
            if (s[i] != '-') {
                return false;
            }
        }
    }
    return true;
}

bool check2(const char* s) {
    // 0,1,2,3,4,12,13,14,15,16,24,25,26,27,28
    // s = 'SE8D0-XXXXX-2K31P-XXXXX-AD648-XXXXX'
    bool z0 = s[0]+s[2]+s[4]+s[13]+s[15]+s[24]+s[26]+s[28] == 486;
    bool z1 = s[0]*s[1]-s[4]+s[12]*s[13]-s[16]+s[24]*s[25]-s[28] == 13713;
    bool z2 = s[3]*s[14]*s[27]-s[2]*s[15]*s[25] == -6256;
    bool z3 = (s[1]-s[3])*s[4] == 48;
    bool z4 = ((s[13]<<3)-(s[15]<<2))*s[14] == 20604;
    bool z5 = ((s[28]<<2)-(s[0]<<2))*s[27] == -5616;

    bool z6 = true;
    for (int i = 0; i < strlen(s); i++) {
        if (i % 12 < 5) {
            if (s[i] > 90 || s[i] < 48 || (s[i] >= 58 && s[i] <= 64)) {
                z6 = false;
            }
        }
    }

    bool z7 = s[4]-s[3]-s[2]-s[1]+s[0]*s[0] == 6744
            && s[16]-s[15]-s[14]-s[13]+s[12]*s[12] == 2405
            && s[28]-s[27]-s[26]-s[25]+s[24]*s[24] == 4107;
    bool z8 = (s[14] < 58)
            && (s[14]+s[24])*(s[28]-s[1]) == -1508;

    return z0 && z1 && z2 && z3 && z4 && z5 && z6 && z7 && z8;
}

int main() { 
    printf("%s\n", BANNER);

    char *serialKey = (char*) malloc(sizeof(char) * 35);
    printf("Enter the serial key to unlock ZZZ Tuning Test qualification: ");
    scanf("%35s", serialKey);
    if (strlen(serialKey) != 35) {
        printf("Invalid serial key.\n");
        return 0;
    }

    // Serial key format: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    // Where X is a character from the set [A-Za-z0-9]
    if (!check1(serialKey)) {
        printf("Invalid serial key.\n");
        return 0;
    }

    // Stage 1: z3 based on sections 1,3,5 of serial key
    // SE8D0-XXXXX-2K31P-XXXXX-AD648-XXXXX
    if (!check2(serialKey)) {
        printf("Invalid serial key.\n");
        return 0;
    }

    // Stage 2: rc4 based on sections 2,4,6 of serial key
    // 6,7,8,9,10,18,19,20,21,22,30,31,32,33,34
    // SE8D0-vsctf-2K31P-4begi-AD648-nnerz

    unsigned char s[256] = {0};
    char key[256] = {"vsCTF is a capture the flag competition organized by Team View Source. vsCTF is meant for players of all skill levels and everyone is welcomed to participate and learn."};
    char pData[512];
    int curr = 0;
    for (int i = 0; i < strlen(serialKey); i++) {
        if (i % 12 >= 6 && i % 12 < 11) {
            pData[curr++] = serialKey[i];
        }
    }
    pData[curr] = '\0';
    unsigned long len = strlen(pData);
    // printf("key : %s\n", key);
    // printf("raw : %s\n", pData);
    
    rc4_init(s, (unsigned char *)key, strlen(key));
    rc4_crypt(s, (unsigned char *)pData, len);

    // printf("encrypt  : %s\n", pData);
    // printf("encrypt64: %s\n", base64_encode(pData, len));
    char* result = base64_encode(pData, len);
    if (strcmp(result, "nRYEZjDuqxtlL8L6EatC") == 0) {
        printf("Congratulations! You have won ZZZ Tuning Test qualification.\n");
        printf("Your flag: ");
        readFlag();
    } else {
        printf("Invalid serial key.\n");
    }

    // rc4_init(s,(unsigned char *)key, strlen(key));
    // rc4_crypt(s,(unsigned char *)pData,len);
    // printf("decrypt  : %s\n",pData);
    
    return 0;
}
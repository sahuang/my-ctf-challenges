#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool check1(int number) {
    double sq = sqrt((double) number);
    return sq == (int) sq;
}

bool check2(int number) {
    if (number == 1) return false;
    if (number == 2) return true;
    if (number % 2 == 0) return false;
    for (int i = 3; i*i <= number; i+=2) {
        if (number % i == 0) return false;
    }
    return true;
}

bool check3(int number) {
    return (number > 0 && number % 2 == 0 && number % 7 == 0);
}

bool check4(int x1, int x2) {
    return x1 < 10 && x2 < 10 && x1 >= 0 && x2 >= 0;
}

bool checker(const char* password, const char* url, int len) {
    int pwd[len];
    for (int i = 0; i < len; i++) {
        pwd[i] = password[i] - '0';
        if (pwd[i] > 9) pwd[i] -= 39;
    }
    return pwd[len/2] == 13 && check3(pwd[len-1]) && 
        check2(1337*pwd[3] + 100) && pwd[0] > 6 && check1(pwd[0]-2) && 
        check4(pwd[1], pwd[6]) && check4(pwd[5], pwd[2]) &&
        pwd[1]+pwd[2]+pwd[5]+pwd[6] == 8 * pwd[1] && pwd[5] >= pwd[6] &&
        check1(pwd[5] - pwd[6] + 4) && pwd[1] > pwd[2] && check2(pwd[1] - pwd[2]) &&
        strlen(url) == 3 && strncmp(url, "@Tm0m3n7!", 3) == 0;
}
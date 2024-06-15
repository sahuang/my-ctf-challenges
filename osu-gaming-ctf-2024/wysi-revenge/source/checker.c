#include <math.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool check1(int a, int b, int c, int d) {
    return a == 22 && b + c == 30 && c * d == 168 && a + b + c + d == 66;
}

bool check2(int a, int b, int c, int d, int e) {
    return a + b + c + d + e == 71 && a * b * c * d * e == 449280 && a * a + b * b == 724
        && c * c + d * d == 313 && e * e == 64 && a + c == 30 && a - d == 5;
}

bool checker(const char* pass, int n) {
    int pwd[n];
    for (size_t i = 0; i < n; i++)
    {
        pwd[i] = pass[i] - 'a';
    }
    return pwd[1] == 0 && pwd[8] == 0 && pwd[11] == 0 && check1(pwd[0], pwd[2], pwd[3], pwd[4])
        && check2(pwd[5], pwd[6], pwd[7], pwd[9], pwd[10]);
}
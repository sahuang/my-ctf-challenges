#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "xxtea.h"
#include "base64.h"

bool checker(const char* password) {
    const char *key = "1145141919810";
    size_t len;
    unsigned char* encrypt_data = xxtea_encrypt(
        password, strlen(password), key, &len);
    char* base64_data = base64_encode(encrypt_data, len);
    return strncmp(base64_data, "Lpg/zsgzznj5i4Ct", len) == 0;
}
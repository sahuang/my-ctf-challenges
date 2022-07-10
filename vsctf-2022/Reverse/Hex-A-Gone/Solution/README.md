# Writeup

The binary is encrypting a flag image and we need to reverse it. A static analysis can reveal what algorithm was used for encryption.

```cpp
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int v3; // edx
  int v4; // ecx
  int v5; // er8
  int v6; // er9
  __int64 v8[3]; // [rsp+10h] [rbp-40h] BYREF
  int v9[2]; // [rsp+28h] [rbp-28h]
  char v10[17]; // [rsp+32h] [rbp-1Eh] BYREF
  unsigned __int64 v11; // [rsp+48h] [rbp-8h]

  v11 = __readfsqword(0x28u);
  ((void (__fastcall *)())((char *)&sub_12C8 + 1))();
  strcpy(v10, "flag.bmp");
  strcpy(&v10[9], "flag.enc.bmp");
  usleep(0xB71B0u);
  ((void (__fastcall *)())((char *)&sub_12C8 + 1))();
  sub_16C7(v8, v10);
  sub_15AB(&v10[9], (int)v10, v3, v4, v5, v6, v8[0], v8[1], (void *)v8[2], v9[0]);
  usleep(0x16E360u);
  ((void (__fastcall *)())((char *)&sub_12C8 + 1))();
  usleep(0xB71B0u);
  ((void (__fastcall *)())((char *)&sub_12C8 + 1))();
  return 0LL;
}
```

`sub_12C8` is printing some text so we can safely ignore that. We can first check `sub_16C7(v8, v10)` which is processing an input image `flag.bmp`.

```cpp
_QWORD *__fastcall sub_16C7(_QWORD *a1, const char *a2)
{
  ...
  sub_1350(&v18, a2);
  v14 = 123LL;
  v15 = calloc(2 * (int)v18 * HIDWORD(v18) - 1, 8uLL);
  for ( i = 0; i < 2 * (int)v18 * HIDWORD(v18) - 1; ++i )
  {
    v14 = sub_131A(v14);
    v15[i] = v14;
  }
  v16 = calloc((int)v18 * HIDWORD(v18), 4uLL);
  for ( j = 0; j < (int)v18 * HIDWORD(v18); ++j )
    v16[j] = j;
  for ( k = v18 * HIDWORD(v18) - 1; k > 0; --k )
  {
    v12 = v15[k] % (unsigned __int64)(k + 1);
    v13 = v16[v12];
    v16[v12] = v16[k];
    v16[k] = v13;
  }
  ptr = calloc(3 * HIDWORD(v18) * (int)v18, 1uLL);
  for ( l = 0; l < (int)v18 * HIDWORD(v18); ++l )
  {
    v2 = &v19[3 * v16[v16[l]]];
    v3 = &ptr[3 * l];
    *(_WORD *)v3 = *(_WORD *)v2;
    v3[2] = v2[2];
  }
  *v19 = *ptr ^ WORD1(v15[(int)v18 * HIDWORD(v18)]);
  v19[1] = ptr[1] ^ 1 ^ BYTE1(v15[(int)v18 * HIDWORD(v18)]);
  v19[2] = ptr[2] ^ 0x41 ^ v15[(int)v18 * HIDWORD(v18)];
  for ( m = 1; m < (int)v18 * HIDWORD(v18); ++m )
  {
    v19[3 * m] = WORD1(v15[HIDWORD(v18) * (int)v18 + m]) ^ ptr[3 * m] ^ v19[3 * m - 3];
    v19[3 * m + 1] = BYTE1(v15[HIDWORD(v18) * (int)v18 + m]) ^ ptr[3 * m + 1] ^ v19[3 * m - 2];
    v19[3 * m + 2] = v15[HIDWORD(v18) * (int)v18 + m] ^ ptr[3 * m + 2] ^ v19[3 * m - 1];
  }
  ...
}
```

With some investigation, `sub_1350(&v18, a2)` is reading and parsing a bmp file. `LODWORD(v11) = (ptr[11] << 8) + ptr[10]` for example, this is getting the "File Offset to PixelArray" (reference [here](https://upload.wikimedia.org/wikipedia/commons/7/75/BMPfileFormat.svg)). `LODWORD(v8)` and `HIDWORD(v8)` are width and height of the image. `v9` stores all rgb values. The returning `a1` is a struct which contains width, height, rgbs, and the pixel offset.

The next part of `sub_16C7` has a bunch of modulo/assignment/xor logics. The function afterwards, `sub_15AB(&v10[9], (int)v10, v3, v4, v5, v6, v8[0], v8[1], (void *)v8[2], v9[0])` is saving the encypted image. So our main task now is to put the encryption algorithm down and write a decryption function.

See below exploit script.

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

// rgb of a pixel
typedef struct {
    unsigned char r;
    unsigned char g;
    unsigned char b;
} pixel_t;

// image info with width, height and pixels
typedef struct {
    int w, h;
    pixel_t *px;
    unsigned char *head;
    int header; // header size
} image_t;

// xor shift 64
uint64_t xorshift64(uint64_t x) {
    x ^= x << 13;
	x ^= x >> 7;
	x ^= x << 17;
	return x;
}

// parse bmp image
image_t parse_bmp(char* fname) {
    unsigned char *rgb;
    image_t x;

    FILE *tempfile = fopen(fname, "rb");
    unsigned char* tmp = malloc(16 * sizeof(unsigned char));
    fread(tmp, sizeof(unsigned char), 16, tempfile);
    x.header = tmp[11] * 256 + tmp[10];
    fclose(tempfile);

    FILE *file = fopen(fname, "rb");
    printf("Header: %d\n", x.header);
    x.head=malloc(x.header * sizeof(unsigned char));
    fread(x.head, sizeof(unsigned char), x.header, file);
    x.w = x.head[19] * 256 + x.head[18];
    x.h = x.head[23] * 256 + x.head[22];

    fseek(file, x.header, SEEK_SET);
    x.px = calloc(x.w * x.h * 3, sizeof(unsigned char));
    rgb = calloc(3, sizeof(unsigned char));
    for(int i = 0; i < x.w * x.h; i++) {
        fread(rgb, 3, 1, file);
        x.px[i].b = rgb[0];
        x.px[i].g = rgb[1];
        x.px[i].r = rgb[2];
    }
    free(rgb);
    fclose(file);
    return x;
}

// write and save an image
void save_bmp(char* output, image_t x) {
    FILE* out = fopen(output, "wb");
    fwrite(x.head, sizeof(unsigned char), x.header, out);
    fseek(out, x.header, SEEK_SET);
    for(int i = 0; i < x.w * x.h; i++)
    {
        fwrite(&x.px[i].b, sizeof(unsigned char), 1, out);
        fwrite(&x.px[i].g, sizeof(unsigned char), 1, out);
        fwrite(&x.px[i].r, sizeof(unsigned char), 1, out);
    }
    fclose(out);
}

// Image decryption algorithm
image_t decrypt_bmp(image_t x) {
	uint64_t key1 = 123;
    uint64_t *a = calloc(x.w * x.h * 2, sizeof(uint64_t));

    // xorshift
    for(int i = 0; i < 2*x.w*x.h; i++)
    {
        key1 = xorshift64(key1);
        a[i] = key1;
    }

    unsigned int *v, r;
    v = calloc(x.w * x.h,sizeof(unsigned int));

    for(int i = 0; i < x.w*x.h; i++) v[i]=i;

    for(int i = x.w*x.h-1; i>=1; i--) {
        r=a[i]%(i+1);
        int tmp = v[r];
        v[r] = v[i];
        v[i] = tmp;
    }

    pixel_t *old;
    old = calloc(x.w*x.h*3, sizeof(unsigned char));
    old[0].r = x.px[0].r^(((a[x.w*x.h]>>8)>>8)&255);
    old[0].g = 1^x.px[0].g^((a[x.w*x.h]>>8)&255);
    old[0].b = 0x41^x.px[0].b^(a[x.w*x.h]&255);
	for(int i=1; i<x.w*x.h; i++) {
		old[i].r=x.px[i-1].r^x.px[i].r^(((a[x.w*x.h+i]>>8)>>8)&255);
		old[i].g=x.px[i-1].g^x.px[i].g^((a[x.w*x.h+i]>>8)&255);
		old[i].b=x.px[i-1].b^x.px[i].b^(a[x.w*x.h+i]&255);
	}

    // Reverse encryption
    unsigned int *vp = calloc(x.w*x.h, sizeof(unsigned int));
    for(int i = 0; i < x.w*x.h; i++) vp[v[i]] = i;
    for(int i = 0; i < x.w*x.h; i++) x.px[i] = old[vp[vp[i]]];
    
    free(old);
    free(v);
    free(a);
    free(vp);
    
    return x;
}

int main(int argc, char *argv[]) {
	image_t x = parse_bmp("flag.enc.bmp");
	char decrypted[] = "flag_decrypted.bmp";
	x = decrypt_bmp(x);
	save_bmp(decrypted, x);
}
```

Recovering the image we can see the flag.

![Flag](./flag.bmp)
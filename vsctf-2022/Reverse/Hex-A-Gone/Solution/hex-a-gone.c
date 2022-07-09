#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

const char FALLGUYS[] =
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿Hex-A-Gone⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠉⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⢀⣠⣶⣶⣶⣶⣤⡀⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⣾⡿⢿⣿⣿⡿⢿⣿⡆⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⠄⢿⣇⣸⣿⣿⣇⣸⡿⠃⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠉⠛⠛⠛⠛⠉⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿⣿\n"
"⣿⣿⣿⡟⠄⠄⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿\n"
"⣿⣿⡟⠄⠄⠄⢠⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣧⠄⠄⠄⠈⢿⣿\n"
"⣿⣿⡇⠄⠄⠄⣾⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣧⠄⠄⠄⠘⣿\n"
"⣿⣿⣇⠄⣰⣶⣿⣿⣿⣦⣀⡀⠄⠄⠄⠄⠄⠄⠄⢀⣠⣴⣿⣿⣿⣶⣆⠄⢀⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⢸⣿⠇⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣴⣾⣿⣶⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n";

const useconds_t delay_per_char = 15000;

void text_animation(const char *txt, useconds_t t) {
	while (*txt) {
		putchar(*txt++);
		fflush(NULL);
		usleep(t);
	}
}

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
    if (!tempfile) {
        exit(1);
    }
    unsigned char* tmp = malloc(16 * sizeof(unsigned char));
    fread(tmp, sizeof(unsigned char), 16, tempfile);
    x.header = tmp[11] * 256 + tmp[10];
    fclose(tempfile);

    FILE *file = fopen(fname, "rb");
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

// Image encryption algorithm
image_t encrypt_bmp(char* input)
{
    image_t x = parse_bmp(input);
    uint64_t key1 = 123;
	uint64_t key2 = 321;
    uint64_t *a = calloc(x.w * x.h * 2, sizeof(uint64_t));

    // xorshift
    for(int i = 0; i < 2 * x.w * x.h; i++)
    {
        key1 = xorshift64(key1);
        a[i] = key1;
    }

	// Swapping
    unsigned int *v, r;
    v = calloc(x.w * x.h, sizeof(unsigned int));
    for(int i = 0; i < x.w * x.h; i++) {
		v[i] = i;
	}
    for(int i = x.w * x.h - 1; i >= 1; i--) {
        r = a[i] % (i+1);
        unsigned int tmp = v[r];
        v[r] = v[i];
        v[i] = tmp;
    }

    // Permutation
    pixel_t *ax = calloc(x.w * x.h * 3, sizeof(unsigned char));
    for(int i = 0; i < x.w * x.h; i++) {
        ax[i]=x.px[v[v[i]]];
	}

    // xorarea
    x.px[0].r = (((key2>>8)>>8)&255)^ax[0].r^(((a[x.w*x.h]>>8)>>8)&255);
    x.px[0].g = ((key2>>8)&255)^ax[0].g^((a[x.w*x.h]>>8)&255);
    x.px[0].b = (key2&255)^ax[0].b^(a[x.w*x.h]&255);
	for(int i = 1; i < x.w * x.h; i++) {
		x.px[i].r = x.px[i-1].r^ax[i].r^(((a[x.w*x.h+i]>>8)>>8)&255);
		x.px[i].g = x.px[i-1].g^ax[i].g^((a[x.w*x.h+i]>>8)&255);
		x.px[i].b = x.px[i-1].b^ax[i].b^(a[x.w*x.h+i]&255);
	}
    free(ax);
    free(a);
    free(v);
    return x;
}

int main(int argc, char *argv[]) {
	text_animation(FALLGUYS, delay_per_char);

	char input[] = "flag.bmp";
	char output[] = "flag.enc.bmp";

	usleep(delay_per_char * 50);
	text_animation("Encrypting flag...\n", delay_per_char * 5);
	image_t x = encrypt_bmp(input);
	save_bmp(output, x);

	usleep(delay_per_char * 100);
	text_animation("Saving encrypted image to flag.enc...\n", delay_per_char * 10);
	usleep(delay_per_char * 50);
	text_animation("Successful!\n", delay_per_char);

	return 0;
}
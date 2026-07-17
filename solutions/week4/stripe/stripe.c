#include "stdio.h"
#include "stdlib.h"

typedef char byte;
typedef struct {
  byte r;
  byte g;
  byte b;
} color;

#define HEIGHT 600
#define WIDTH 800
#define LINES 5
#define FILE_PATH "image.ppm"

int main(void) {

  FILE *f = fopen(FILE_PATH, "wb");
  fprintf(f, "P6\n");
  fprintf(f, "%d %d\n", WIDTH, HEIGHT);
  fprintf(f, "255\n");

  color image[HEIGHT][WIDTH] = {0x00};

  for (int y = 0; y < HEIGHT; y++) {
    for (int x = 0; x < WIDTH; x++) {
      const color red = {0xff, 0x00, 0x00};
      const color blue = {0x00, 0x00, 0xff};
      if ((y / (HEIGHT / LINES)) % 2 != 0) {
        fputc(red.r, f);
        fputc(red.g, f);
        fputc(red.b, f);
      } else {
        fputc(blue.r, f);
        fputc(blue.g, f);
        fputc(blue.b, f);
      }
    }
  }

  system("sha256sum image.ppm");

  fclose(f);

  return 0;
}

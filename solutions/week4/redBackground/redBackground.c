#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define WIDTH 800
#define HEIGHT 600
#define IMAGE_PATH "image.ppm"

typedef char byte;
typedef struct {
  byte red;
  byte green;
  byte blue;
} color;

int main(void) {

  FILE *image = fopen(IMAGE_PATH, "wb");

  fprintf(image, "P6 \n");
  fprintf(image, "%d %d\n", WIDTH, HEIGHT);
  fprintf(image, "255\n");

  color pixels[HEIGHT][WIDTH];

  for (int y = 0; y < HEIGHT; y++) {
    for (int x = 0; x < WIDTH; x++) {
      pixels[y][x] = (color){0xFF, 0x00, 0x00};
    }
  }

  fwrite(pixels, sizeof(pixels), 1, image);
  char temp[100] = "sha256sum ";
  strcat(temp, IMAGE_PATH);
  system(temp);

  fclose(image);

  return 0;
}

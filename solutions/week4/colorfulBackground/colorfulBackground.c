#include "stdio.h"
#include "stdlib.h"
#include <ctype.h>
#include <string.h>

#define WIDTH 800
#define HEIGHT 600

typedef char byte;
typedef struct {
  byte red;
  byte green;
  byte blue;
} color;

color colorParser(const char *inputColor);
int findFirstIndex(const char *input, char target);

int main(int argc, char **argv) {

  if (argc != 2) {
    printf("Usage: ./background [hex color]\n");
    return 1;
  }

  const char *hexColor = argv[1];

  if (strlen(hexColor) != 6) {
    printf("invalid hexColor's length\n");
    return 1;
  }

  FILE *image = fopen("image.ppm", "wb");
  if (image == NULL) {
    printf("cannot create file\n");
    return 1;
  }

  fprintf(image, "P6 \n");
  fprintf(image, "%d %d\n", WIDTH, HEIGHT);
  fprintf(image, "255\n");

  color pixels[HEIGHT][WIDTH];
  color base = colorParser(hexColor);

  for (int y = 0; y < HEIGHT; y++) {
    for (int x = 0; x < WIDTH; x++) {
      pixels[y][x] = base;
    }
  }

  fwrite(pixels, sizeof(pixels), 1, image);
  system("sha256sum image.ppm");

  return 0;
}

color colorParser(const char *inputColor) {
  const char *hex = "0123456789abcdef";
  int temp[3] = {0};
  for (int i = 0, arrayIndex = 0; i < strlen(inputColor);
       i += 2, arrayIndex++) {
    int sum = 0;
    int index = findFirstIndex(hex, inputColor[i + 1]);
    int index1 = findFirstIndex(hex, inputColor[i]);
    if (index == -1 || index1 == -1) {
      printf("cannot create color!\n");
      exit(1);
    }

    sum += 1 * index;
    sum += 16 * index1;
    temp[arrayIndex] = sum;
  }

  return (color){temp[0], temp[1], temp[2]};
}

int findFirstIndex(const char *input, char target) {
  target = tolower(target);
  for (int i = 0; i < strlen(input); i++) {
    if (target == input[i]) {
      return i;
    }
  }
  return -1;
}

#include "stdio.h"
#include <stdlib.h>

#define WIDTH 800
#define HEIGHT 800
#define FILE_PATH "image.ppm"

typedef char byte;
typedef struct {
  byte r;
  byte g;
  byte b;
} color;

void generateGradientData(int n, int buffer[n][n]);
void putColor(FILE *stream, color input);
void paintGradient(FILE *f, const int size);

int main(void) {
  FILE *image = fopen(FILE_PATH, "wb");
  if (image == NULL) {
    printf("cannot open file");
    return 1;
  }

  fprintf(image, "P6 \n");
  fprintf(image, "%d %d\n", WIDTH, HEIGHT);
  fprintf(image, "255\n");

  paintGradient(image, 5);

  system("sha256sum image.ppm");

  fclose(image);

  return 0;
}

void paintGradient(FILE *f, const int size) {
  const int highestNumber = size * 2 - 1;
  const int offset = 0x10;
  int squareSize = WIDTH / size;
  color baseColor = {0x10, 0x00, 0xf0};
  color gradients[highestNumber];

  for (int i = 0, localOffset = offset; i < highestNumber;
       i++, localOffset += offset) {
    gradients[i].r = baseColor.r + localOffset;
    gradients[i].g = baseColor.g;
    gradients[i].b = baseColor.b;
  }

  int data[size][size];
  generateGradientData(size, data);

  for (int i = 0; i < WIDTH; i++) {
    for (int j = 0; j < WIDTH; j++) {
      int currentX = j / squareSize;
      int currentY = i / squareSize;
      putColor(f, gradients[data[currentY][currentX] - 1]);
    }
  }
}

void generateGradientData(int n, int buffer[n][n]) {
  // clear garbage value
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      buffer[i][j] = 0;
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0, value = i + 1; j < n; j++, value++) {
      buffer[i][j] = value;
    }
  }
}

void putColor(FILE *stream, color input) {
  fputc(input.r, stream);
  fputc(input.g, stream);
  fputc(input.b, stream);
}

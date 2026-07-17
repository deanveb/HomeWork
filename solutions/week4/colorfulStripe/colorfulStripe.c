#include "ctype.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef char byte;
typedef struct {
  byte r;
  byte g;
  byte b;
} color;

#define HEIGHT 600
#define WIDTH 800
#define FILE_PATH "image.ppm"

color colorParser(const char *inputColor);
int findFirstIndex(const char *input, char target);
int numberParser(const char *inputNumber, unsigned int base,
                 const char *digits);
int power(int a, int b);
byte isNumber(char *inputNumber);

int main(int argc, char **argv) {
  if (argc != 4) {
    printf("Usage: [number of lines] [color 1] [color 2]\n");
    return 1;
  }

  const char *hexColor1 = argv[2];
  const char *hexColor2 = argv[3];

  if (!isNumber(argv[1])) {
    printf("line has to be a number\n");
    return 1;
  }

  const int line = numberParser(argv[1], 10, "0123456789");

  if (line > 20 || line <= 0) {
    printf("%d is too big\n", line);
    return 1;
  }

  if (strlen(hexColor1) != 6 || strlen(hexColor2) != 6) {
    printf("1 of 2 color has invalid length\n");
    return 1;
  }

  FILE *f = fopen(FILE_PATH, "wb");
  if (f == NULL) {
    printf("cannot open or create file\n");
    return 1;
  }
  fprintf(f, "P6\n");
  fprintf(f, "%d %d\n", WIDTH, HEIGHT);
  fprintf(f, "255\n");

  color color1 = colorParser(hexColor1);
  color color2 = colorParser(hexColor2);

  for (int y = 0; y < HEIGHT; y++) {
    for (int x = 0; x < WIDTH; x++) {
      if ((y / (HEIGHT / line)) % 2 == 0) {
        fputc(color1.r, f);
        fputc(color1.g, f);
        fputc(color1.b, f);
      } else {
        fputc(color2.r, f);
        fputc(color2.g, f);
        fputc(color2.b, f);
      }
    }
  }

  system("sha256sum image.ppm");

  fclose(f);

  return 0;
}

color colorParser(const char *inputColor) {
  const char *hex = "0123456789abcdef";
  int temp[3] = {0};

  for (int i = 0, arrayIndex = 0; i < strlen(inputColor);
       i += 2, arrayIndex++) {
    char number[3] = {inputColor[i], inputColor[i + 1], '\0'};
    int sum = numberParser(number, 16, hex);

    temp[arrayIndex] = sum;
  }

  return (color){temp[0], temp[1], temp[2]};
}

int numberParser(const char *inputNumber, unsigned int base,
                 const char *digits) {
  int sum = 0;
  for (int i = strlen(inputNumber) - 1, n = strlen(inputNumber); i >= 0; i--) {
    int index = findFirstIndex(digits, inputNumber[i]);
    if (index == -1) {
      printf("cannot convert %s to base %d\n", inputNumber, base);
      exit(1);
    }

    sum += power(base, n - i - 1) * index;
  }

  return sum;
}

int power(int a, int b) {
  int result = 1;

  for (int i = 0; i < b; i++) {
    result *= a;
  }

  return result;
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

byte isNumber(char *inputNumber) {
  for (int i = 0, n = strlen(inputNumber); i < n; i++) {
    if (!isdigit(inputNumber[i])) {
      return 0;
    }
  }
  return 1;
}

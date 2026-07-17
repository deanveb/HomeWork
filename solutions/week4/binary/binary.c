#include "stdio.h"

#define HEX_STRING_LEN 2

void decToHex(unsigned char input, char output[HEX_STRING_LEN]);

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("Usage: ./binary input.txt\n");
    return 1;
  }

  FILE *f;
  f = fopen(argv[1], "rb");
  if (f == NULL) {
    printf("cannot open file\n");
    return 2;
  }
  unsigned char buffer = 0;
  while (fread(&buffer, 1, 1, f)) {
    char result[HEX_STRING_LEN + 1];
    decToHex(buffer, result);
    printf("%s ", result);
  }
  printf("\n");

  fclose(f);

  return 0;
}

void decToHex(unsigned char input, char output[HEX_STRING_LEN + 1]) {
  char *hexString = "0123456789abcdef";

  for (int i = HEX_STRING_LEN - 1; i >= 0; i--) {
    output[i] = hexString[input % 16];
    input /= 16;
  }

  output[HEX_STRING_LEN] = '\0';
}

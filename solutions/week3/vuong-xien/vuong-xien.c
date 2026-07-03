#include "cs50.h"
#include "stdio.h"

int printDiagonal(int size, int y, int x, int numberToPrint,
                  int buffer[size][size]);

int main(void) {
  int n = 0;
  do {
    n = get_int("size: ");
  } while (n <= 0);

  int buffer[n][n];
  // clear garbage value
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      buffer[i][j] = 0;
    }
  }
  int count = 1;
  for (int i = 0; i < n; i++) {
    if (printDiagonal(n, i, 0, count, buffer) == -1)
      return 1;
    count++;
  }

  for (int j = 1; j < n; j++) {
    if (printDiagonal(n, n - 1, j, count, buffer) == -1)
      return 1;
    count++;
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      printf("%d", buffer[i][j]);
    }
    printf("\n");
  }
}

int printDiagonal(int size, int y, int x, int numberToPrint,
                  int buffer[size][size]) {
  // if (y < 0 || x < 0 || y >= size || x >= size)
  //   return -1;
  do {
    buffer[y][x] = numberToPrint;
    y--;
    x++;
  } while (y >= 0 && x < size);

  return 0;
}

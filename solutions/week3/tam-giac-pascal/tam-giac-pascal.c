#include "cs50.h"
#include "stdio.h"

int main(void) {
  int n;

  do {
    n = get_int("size: ");
  } while (n <= 0);

  int buffer[n][n];

  // clear buffer garbage value
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      buffer[i][j] = 0;
    }
  }
  buffer[0][0] = 1;

  for (int i = 1; i < n; i++) {
    for (int j = 0; j < i + 1; j++) {
      // Check for out of bound
      int firstValue = (i - 1 < 0 || j - 1 < 0) ? 0 : buffer[i - 1][j - 1];
      int secondValue = (i - 1 < 0 || j < 0) ? 0 : buffer[i - 1][j];

      buffer[i][j] = firstValue + secondValue;
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i + 1; j++) {
      printf((j + 1 >= i + 1) ? "%d" : "%d ", buffer[i][j]);
    }
    printf("\n");
  }

  return 0;
}

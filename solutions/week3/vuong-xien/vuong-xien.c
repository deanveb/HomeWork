#include "cs50.h"
#include "stdio.h"

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

  for (int i = 0; i < n; i++) {
    for (int j = 0, value = i + 1; j < n; j++, value++) {
      buffer[i][j] = value;
    }
  }

  // Print result
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      printf("%d", buffer[i][j]);
    }
    printf("\n");
  }
}

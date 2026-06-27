#include "cs50.h"
#include "stdio.h"

int main(void) {
  int n = 0;
  do {
    n = get_int("số:");
    if (n != 0)
      printf("%d\n", n * n);
  } while (n != 0);

  return 0;
}

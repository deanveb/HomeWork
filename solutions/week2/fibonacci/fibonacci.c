#include "cs50.h"
#include "stdio.h"

int main(void) {
  int n = 0;
  do {
    n = get_int("thứ tự fibonacci:");
  } while (n <= 0);

  int first = 1;
  int second = 1;
  int temp = 0;

  for (int i = 2; i < n; i++) {
    temp = first + second;
    first = second;
    second = temp;
  }
  printf("%d", second);

  return 0;
}

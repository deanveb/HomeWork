#include "cs50.h"
#include <stdbool.h>
#include <stdio.h>

bool isPrime(int number);

int main(void) {
  int n = 0;
  do {
    n = get_int("Nhập số:");
  } while (n < 0);

  if (isPrime(n)) {
    printf("YES\n");
  } else {
    printf("NO\n");
  }
}

bool isPrime(int number) {
  if (number == 0 || number == 1)
    return false;
  for (int i = 2; i < number; i++) {
    if (number % i == 0)
      return false;
  }
  return true;
}

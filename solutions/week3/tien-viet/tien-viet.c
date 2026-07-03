#include "cs50.h"
#include "stdio.h"

#define MAX_CASH_TYPE 12

int main() {
  int cash;
  do {
    cash = get_int("số tiền: ");
  } while (cash < 0);

  int cashType[MAX_CASH_TYPE] = {100,   200,   500,   1000,   2000,   5000,
                                 10000, 20000, 50000, 100000, 200000, 500000};
  int count = 0;
  int currentCashType = MAX_CASH_TYPE - 1;
  while (cash > 0) {
    if (cash < cashType[currentCashType]) {
      currentCashType--;
      continue;
    }

    cash -= cashType[currentCashType];
    count++;
  }

  printf("%d\n", count);
  return 0;
}

#include "cs50.h"
#include "stdio.h"
#include <ctype.h>
#include <string.h>

bool isPalindrome(string input);
bool isAllWords(string input);

int main(void) {
  string text;
  do {
    text = get_string("message: ");
  } while (strlen(text) <= 0 || !isAllWords(text));

  if (isPalindrome(text)) {
    printf("YES\n");
  } else {
    printf("NO\n");
  }

  return 0;
}

bool isPalindrome(string input) {
  for (int i = 0, n = strlen(input); i < n / 2; i++) {
    if (tolower(input[i]) != tolower(input[n - i - 1])) {
      return false;
    }
  }
  return true;
}

bool isAllWords(string input) {
  for (int i = 0, n = strlen(input); i < n; i++) {
    if (!isalpha(input[i])) {
      return false;
    }
  }
  return true;
}

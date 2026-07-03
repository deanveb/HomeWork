#include "cs50.h"
#include "stdio.h"
#include <ctype.h>
#include <string.h>

#define WORD_COUNT 26

bool isAllWords(string input);

int main(void) {
  string text = "";
  do {
    text = get_string("message: ");
  } while (strlen(text) <= 0 || !isAllWords(text));

  int buffer[WORD_COUNT];
  // clear garbage value
  for (int i = 0; i < WORD_COUNT; i++) {
    buffer[i] = 0;
  }

  for (int i = 0, n = strlen(text); i < n; i++) {
    buffer[tolower(text[i]) - 97]++;
  }

  for (int i = 0; i < WORD_COUNT; i++) {
    if (buffer[i] <= 0) {
      continue;
    }
    printf("%c:%d ", i + 97, buffer[i]);
  }
  printf("\n");

  return 0;
}

// chỉ nhận chữ và space
bool isAllWords(string input) {
  for (int i = 0, n = strlen(input); i < n; i++) {
    if (!isalpha(input[i]) && input[i] != ' ') {
      return false;
    }
  }
  return true;
}

#include "cs50.h"
#include "stdio.h"
#include <string.h>

#define WORD_COUNT 256

int main() {
  string text = "";
  do {
    text = get_string("message: ");
  } while (strlen(text) <= 0);

  char result[strlen(text) + 1];
  bool buffer[WORD_COUNT];
  for (int i = 0; i < WORD_COUNT; i++) {
    buffer[i] = false;
  }

  int result_length = 0;
  for (int i = 0, n = strlen(text); i < n; i++) {
    if (buffer[text[i]] == true) {
      continue;
    }
    if (text[i] != ' ') {
      buffer[text[i]] = true;
    }
    result[result_length] = text[i];
    result_length++;
  }
  result[result_length] = '\0';
  printf("%s\n", result);

  return 0;
}

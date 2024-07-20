#include <stdio.h>

int main(void) {
  char *hey = "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx";

  for (int i = 0; i < 48; i = i + 1) {
    hey[i] = hey[i] ^ 5;
    printf("%c", hey[i]);
  };
  return 0;
}
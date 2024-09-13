#include <stdio.h>

int main(void) {
  char *hey = "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx";
  int nuhuh[49] = {0};

  printf("I'm alive");
  for (int i = 0; i < sizeof(hey); i++) {
    
    nuhuh[i] = hey[i] ^ 5;
    printf("%c is %c", hey[i], nuhuh[i]);

  };
  return 0;
}

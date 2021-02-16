#include <stdio.h>
#include <stdlib.h>

#define N 16 /* buffer size */

int main(void) {
  char name[N]; /* buffer */
  
  /* pregunta l usuario por su nombre */
  printf("Como te llamas? ");
  scanf("%s", name);
  
  printf("Hola, %s!\n", name); /* greet the user */
  
  return EXIT_SUCCESS;
}

/*Compilacion con gcc*/
/* gcc nombre.c -Wall -Wextra -Wshadow -pedantic -std=c11 -g3 -o nombre */

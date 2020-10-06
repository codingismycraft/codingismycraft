/* Write a program that replaces tabs in the input with the proper number
of blanks to space to the next tab stop.

to build: gcc -g ex_01_20.c -o ex_01_20
to test: cat text | ex_01_20
*/
#include <stdio.h>

#define TAB_LENGTH 8


int main() {
    int c;
    int length = 0;
    int i, j;

    while( (c=getchar()) != EOF ){
        if (c == '\t') {
          j =  TAB_LENGTH - (length % TAB_LENGTH);
          for(i = 0; i <j; ++i)
            putchar(' ');
            length = 0;
        }
        else if (c == '\n') {
            putchar(c);
            length = 0;
        }
        else {
            putchar(c);
            length += 1;
        }
    }
}

/* Write a program to copy its input to its output replacing one or more
blanks by a single one.

to build: gcc ex_01_09.c -o ex_01_09
to test: cat ex_01_09.c | ex_01_09
*/
#include <stdio.h>

int main() {
    int c;
    int blanks=0;
    while ( (c = getchar()) != EOF) {
        if (c ==' ')
            blanks +=1;
        else
            blanks = 0;
        if (blanks <= 1)
            putchar(c);
    }
}

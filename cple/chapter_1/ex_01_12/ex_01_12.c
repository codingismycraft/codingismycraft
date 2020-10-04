/* Write a program that prints its input one word per line.

to build: gcc ex_01_12.c -o ex_01_12
to test: cat text | ex_01_12
*/
#include <assert.h>
#include <stdio.h>

#define INSIDE_A_WORD 1
#define OUTSIDE_A_WORD 0


int main() {
    int c;
    int state = OUTSIDE_A_WORD;

    while ( (c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n'){
            if (state == INSIDE_A_WORD)
                putchar('\n');
            state = OUTSIDE_A_WORD;
        }
        else {
            state = INSIDE_A_WORD;
            putchar(c);
        }
    }
    putchar('\n');
}

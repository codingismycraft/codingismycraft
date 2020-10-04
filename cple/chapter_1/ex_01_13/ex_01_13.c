/* Write a program to print a histogram of the lengths of the words in its
input.
    `
to build: gcc ex_01_13.c -o ex_01_13
to test: cat text | ex_01_13
*/
#include <assert.h>
#include <stdio.h>

#define INSIDE_A_WORD 1
#define OUTSIDE_A_WORD 0
#define MAX_LENGTH 15

int main() {
    int c;
    int state = OUTSIDE_A_WORD;
    int word_length = 0;
    int length = 0;
    int frequencies[MAX_LENGTH];
    int i, j;

    for(i=0; i < MAX_LENGTH; ++i)
        frequencies[i] = 0;

    while ( (c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n'){
            if (state == INSIDE_A_WORD) {
                assert (1 <= length <= MAX_LENGTH);
                frequencies[length-1] += 1;
                length = 0;
                state = OUTSIDE_A_WORD;
            }
        }
        else {
            state = INSIDE_A_WORD;
            if (length < MAX_LENGTH)
                length +=1;
        }
    }

    if (length > 0)
        frequencies[length-1] += 1;

    putchar('\n');
    for(i=0; i < MAX_LENGTH; ++i)
    {
        printf("%2i ", i+1);
        for(j=0; j < frequencies[i]; ++j)
            putchar('*');
        putchar('\n');
    }
}

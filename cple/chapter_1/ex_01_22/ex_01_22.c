/* Write a program to "fold" long input lines into two or more shorter lines
after the last non-blank character that occurs before the n-th column of
input. Make sure your program does something intelligent with very long line,
and if there are no blanks or tabs before the specified column.


to build: gcc -g ex_01_22.c -o ex_01_22
to test: cat text | ex_01_22
*/

#include <stdio.h>


#define MAX_LENGTH 20
#define TAB_SIZE 8

int main(void)
{
    int c, i;
    int line_length = 0;

    while ((c = getchar()) != EOF) {
        switch (c) {
            case '\n':
                line_length += 1;
                putchar(c);
                break;
            case '\t':
                for(i = 0; i < TAB_SIZE; ++i){
                    if (line_length >= MAX_LENGTH) {
                        putchar('\n');
                        line_length = 0;
                    }
                    line_length += 1;
                    putchar(' ');
                }
                break;
            default:
                if (line_length >= MAX_LENGTH) {
                    putchar('\n');
                    line_length = 0;
                }
                line_length += 1;
                putchar(c);
        }
    }
    return 0;
}

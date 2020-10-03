/* Write a program to copy its input to its output replacing
each tab with \t, each backspace with \b and each backslash with \\.

to build: gcc ex_01_10.c -o ex_01_10
to test: cat ex_01_10.c | ex_01_10
*/
#include <stdio.h>

int main() {
    int c;
    int blanks=0;
    while ( (c = getchar()) != EOF) {
        switch (c){
            case '\t':
                printf("\\t");
                break;
            case '\b':
                printf("\\b");
                break;
            case '\\':
                printf("\\\\");
                break;
             default:
                putchar(c);
        }
    }
}

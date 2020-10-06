/* Write a program that replaces string of blanks by the minimum number
of tabs and spaces to achieve the same spacing.

to build: gcc -g ex_01_21.c -o ex_01_21
to test: cat text | ex_01_21
*/
#include <stdio.h>

#define TAB_LENGTH 8

void putspaces(int tabs, int spaces){
    int i;

    tabs += spaces / TAB_LENGTH;
    spaces = spaces % TAB_LENGTH;

    for (i = 0; i < tabs; ++i)
        putchar('\t');

    for (i = 0; i < spaces; ++i)
        putchar(' ');
}

int main() {
    int c, i, j, tabs, spaces;
    tabs = spaces = 0;

    while( (c=getchar()) != EOF ){
        switch (c) {
            case '\t':
                tabs += 1;
                break;
            case ' ':
                spaces += 1;
                break;
            case '\n':
                if (tabs > 0 || spaces > 0)
                    putspaces(tabs, spaces);
                putchar(c);
                tabs = spaces = 0;
                break;
            default:
                if (tabs > 0 || spaces > 0)
                    putspaces(tabs, spaces);
                putchar(c);
                tabs = spaces = 0;
        }
    }
}

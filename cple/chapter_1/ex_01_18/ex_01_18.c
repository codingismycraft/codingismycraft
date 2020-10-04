/* Write a program to remove trailing blanks and tabs from each line of input
and to delete entirely blank lines.

to build: gcc ex_01_18.c -o ex_01_18
to test: cat text | ex_01_18
*/
#include <stdio.h>

int main() {
    int trailing_blanks = 0;
    int c = 0;
    int i;
    int length = 0;
    while ( (c=getchar()) != EOF){
        if(c == ' ' || c == '\t')
            trailing_blanks++;
        else if (c == '\n') {
            for(i=0; i < trailing_blanks; ++i)
                putchar('\b');
            trailing_blanks = 0;
            if (length > 0)
                putchar(c);
            length = 0;
        }
        else {
            trailing_blanks = 0;
            length++;
            putchar(c);
        }
    }
}

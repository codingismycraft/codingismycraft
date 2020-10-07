/* Write a program to remove all comments from a C program. Don't forget to
handle quoted strings and character constants properly.

to build: gcc -g ex_01_23.c -o ex_01_23
to test: cat test.c | ex_01_23
*/

#include <assert.h>
#include <stdio.h>

#define INSIDE_SINGLE_LINE_COMMENT 1
#define INSIDE_MULTI_LINE_COMMENT 2
#define INSIDE_STRING 3
#define IN_CODE 4

#define CLOSING_SINGLE_LINE_COMMENT = "\n";
#define CLOSING_MULTI_LINE_COMMENT = "*/"
#define CLOSING_STRING = "\"";

int state = IN_CODE;

int get_next_char(int c1){
    int c2;
    if (c1 == EOF)
        return EOF;
    switch (state) {
        case INSIDE_SINGLE_LINE_COMMENT:
            if (c1 == '\n'){
                putchar('\n');
                state = IN_CODE;
             }
             return getchar();
        case INSIDE_MULTI_LINE_COMMENT:
            if (c1 != '*')
                return getchar();
            c2 = getchar();
            if (c2 == EOF)
                return EOF;
            else if (c2 == '/')
                state = IN_CODE;
            return getchar();
        case INSIDE_STRING:
            if (c1 == '\\') {
                putchar(c1);
                c2 = getchar();
                if (c2 == EOF)
                    return EOF;
                putchar(c2);
                return getchar();
            }
            else if (c1 == '"')
                state = IN_CODE;
            putchar(c1);
            return getchar();
        default:
            assert (state == IN_CODE);
            if (c1 == '"') {
                state = INSIDE_STRING;
                putchar(c1);
            }
            else if (c1 == '/') {
                c2 = getchar();
                if (c2 == '/'){
                    state = INSIDE_SINGLE_LINE_COMMENT;
                }
                else if (c2 == '*') {
                    state = INSIDE_MULTI_LINE_COMMENT;
                }
                else {
                    putchar(c1);
                    if (c2 == EOF)
                        return EOF;
                    putchar(c2);
                    return getchar();
                }
            }
            else {
                putchar(c1);
            }
            return getchar();
    }
}

int main(void)
{
    int c;

    c = getchar();

    while ((c = get_next_char(c)) != EOF) {

    }
    return 0;
}

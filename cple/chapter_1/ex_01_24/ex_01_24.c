/* Write to check a C program for rudimentary syntax errors like unbalanced
parentheses, brackets and braces.

to build: gcc -g ex_01_24.c -o ex_01_24
to test: cat test.c | ex_01_24 or
cat test1.c | ex_01_24
*/

#include <assert.h>
#include <stdio.h>

#define TRUE 1
#define FALSE 0

int main() {
    int brackets = 0;
    int parentheses = 0;
    int braces = 0;
    int c;
    int in_string = FALSE;
    int escaped_char = FALSE;
    int lines_count = 0;

    while ( (c = getchar()) != EOF) {
        putchar(c);
        if (c == '\n')
            lines_count++;
        
        if (escaped_char){
            escaped_char = FALSE;
            continue;
        }

        switch (c) {
            case '[':
                if (!in_string){
                    braces++;
                }
                break;
            case '(':
                if (!in_string){
                    parentheses++;
                }
                break;
            case '{':
                if (!in_string)
                    brackets++;
                break;
            case '}':
                if (!in_string){
                    assert(brackets > 0);
                    brackets--;
                }
                break;
            case ')':
                if (!in_string){
                    assert(parentheses> 0);
                    parentheses--;
                }
                break;
            case ']':
                if (!in_string){
                    braces--;
                }
                break;
            case '"':
                in_string = !in_string;
                break;
            case '\\':
                if(in_string) {
                    escaped_char = TRUE;
                }
                break;
            default:
                break;
        }
    }

    printf("brackets: %i\n", brackets);
    printf("parentheses: %i\n", parentheses);
    printf("braces: %i\n", braces);
    printf("lines count: %i\n", lines_count);

    assert(brackets == 0);
    assert(parentheses == 0);
    assert(braces == 0);
}

/* Write a program to print all input lines that are longer than 80 characters.

to build: gcc ex_01_17.c -o ex_01_17
to test: cat text | ex_01_17
*/
#include <stdio.h>

#define CUTOFF_LENGTH 80


int main() {
    int c;
    int cur_length = 0;
    char buffer[CUTOFF_LENGTH + 1];

    while ( (c=getchar()) != EOF){
        if (c != '\n'){
            if (cur_length < CUTOFF_LENGTH) {
               buffer[cur_length++] = c;
            }
            else if (cur_length == CUTOFF_LENGTH){
                buffer[cur_length++] = '\0';
                printf("%s", buffer);
                putchar(c);
            }
            else {
                putchar(c);
            }
        }
        else {
            if (cur_length >= CUTOFF_LENGTH)
                putchar(c);
            cur_length = 0;
        }
    }
}

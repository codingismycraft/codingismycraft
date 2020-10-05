/* Write a program that reverses its input a line at a time.

to build: gcc -g ex_01_19.c -o ex_01_19
to test: cat text | ex_01_19
*/
#include <stdio.h>

#define MAX_STR_LENGTH 100

void reverse(char* s);
int getline1(char s[], int n);

void reverse(char* s){
    int l = 0;
    int i = 0;
    char t = 0;

    while(s[l++] != '\0');
    l--;
    for (i=0; i < l/2; ++i){
        t = s[l-i-1];
        s[l-i-1] = s[i];
        s[i] = t;
    }
}

int getline1(char s[], int n) {
    int i = 0;
    int c = 0;

    while ( (c=getchar()) != EOF && i < n -2) {
        s[i++] = c;
        if (c == '\n')
            break;
    }
    s[i] = '\0';
    return i;
}

int main() {
    char buffer[MAX_STR_LENGTH];
    int l = 0;
    while(l=getline1(buffer, MAX_STR_LENGTH)){
        reverse(buffer);
        printf("%s", buffer);
    }
}

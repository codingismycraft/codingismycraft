/* Write a version of itoa that accepts three arguments 
 * instead of two. The third argument is a minimum field 
 * width; the converted number must be padded with 
 * blanks on the left if necessary to make it wide enough.
 * 
* to build: gcc -g ex_03_06.c -o ex_03_06   
 * */

#include <stdio.h>
#include <limits.h>
#include <assert.h>
#include <string.h>

char buffer[64];

#define NUMBER char 


void reverse(char s[]){
    int i = 0;
    int j = strlen(s) - 1;
    int c;

    while( i < j ){
        c = s[i];
        s[i] = s[j];
        s[j] = c;
        ++i, --j;
    }
}


NUMBER abs_val(NUMBER v){
    return v >= 0 ? v : -1 * v;
}

void itoa(NUMBER n, char s[], int width){
    int i;
    int sign = n;
    i = 0;
    do {
        s[i++] = abs_val(n % 10) + '0';
    } while ( (n/=10) != 0);

    if (sign < 0)
        s[i++] = '-';

    for(; i < width; i++)
        s[i] =' ';

    s[i] = '\0';
    reverse(s);
}


int main(){
    NUMBER i = -128;

    itoa(i, buffer, 12);
    printf("%s\n", buffer);
}


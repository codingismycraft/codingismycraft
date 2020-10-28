/* 
 * Write the function itob(n,s,b) that converts the 
 * integer n into a base b character representation 
 * in the string s. 
 *
 * In particular, itob(n,s,16) formats s as a 
 * hexadecimal integer in s.
 *
 * to build: gcc -g ex_03_05.c -o ex_03_05   
 */

#include<stdio.h>
#include<string.h>

#define BUFFER_SIZE 100

void itob(int n, char buffer[], int base);
void reverse(char s[]);

void itob(int n, char buffer[], int base){
    int pos = 0;
    int r;
    const int is_negative = (n < 0);

    while(n){
        r = n % base;
        if(r <0)
            r = -r;
        buffer[pos++] = (r <= 9 ? '0' + r : 'A' + r - 10);
        n = n / base;
    }
    if (is_negative)
        buffer[pos++] = '-';

    buffer[pos] = '\0';
    reverse(buffer);
}


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


int main(void){
    int number,base;
    char buffer[BUFFER_SIZE];

    number= -18234;
    base=16;
    itob(number, buffer, base);
    printf("%s\n", buffer);
    return 0;
}



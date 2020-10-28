/*  In a two’s complement number representation, our version 
 *  of itoa does not handle the largest negative number, that is, 
 *  the value of n equal to -(2^wordsize-1). Explain why not. 
 *  Modify it to print that value correctly, 
 *  regardless of the machine on which it runs.
 *
 * to build: gcc -g ex_03_04.c -o ex_03_04   
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

// Book's version of itoa...
void original_itoa(NUMBER n, char s[]){
    int i;
    int sign = n;
    if (sign < 0)
        n = -n;
    /* If n happens to be the minimum possible value, 
     * which will be -2^(n-1) where n is the number of 
     * the bits in the type NUMBER then multiplying it by
     * -1 will not convert it to a positive value.  This
     * happens because the maximum positive value is
     * 2^(n-1) - 1 so the behaviour is undefined. 
     * */

    i = 0;
    do {
        s[i++] = n % 10 + '0';
    } while (  (n/=10) > 0 );
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}

NUMBER abs_val(NUMBER v){
    return v >= 0 ? v : -1 * v;
}

void itoa(NUMBER n, char s[]){
    /* Improved version that can handle the minimum value.*/
    int i;
    int sign = n;
    i = 0;
    do {
        s[i++] = abs_val(n % 10) + '0';
    } while ( (n/=10) != 0);
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}


int main(){
    NUMBER i = -128;
    original_itoa(i, buffer);
    printf("%s\n", buffer);

    itoa(i, buffer);
    printf("%s\n", buffer);
}


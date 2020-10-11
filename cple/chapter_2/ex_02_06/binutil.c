/* Implements binary utilities.*/

#include <stdio.h>
#include <limits.h>
#include <assert.h>

char buffer[64];


#define NUMBER unsigned char

void num2bin(NUMBER c, char buffer[]){
    const int n = sizeof(c) * CHAR_BIT;
    int i;

    buffer[n] = '\0';
    for(i= n - 1; i >=0; --i, c = c >> 1)
        buffer[i] = c & 1 ? '1' : '0';

}

NUMBER bin2num(char buffer[]){
    int n = 0, i;
    NUMBER value = 0, factor = 1;

    while (buffer[n++] != '\0');

    for(i=n-2; i >=0; --i){
        value += factor * (buffer[i] - '0');
        factor *=2;
    }
    return value;
}


int main(){
    NUMBER r = 127;
    num2bin(r, buffer);
    printf("%s\n", buffer);
    printf("%d\n", bin2num(buffer));
}

/* Write a function `invert(x, p, n)` that returns x with the n
bits that begin at position p inverted (i.e. changed into 0 and
vice versa), leaving the others unchanged.

to build: gcc -g ex_02_07.c -o ex_02_07
*/

#include <assert.h>

#define NUMBER unsigned char

NUMBER invert(NUMBER x, int p, int n){
    NUMBER y = ~0;

    y = y << n;
    y = ~y;
    y = y << (p + 1 -n);

    return x ^ y;
}

int main(){
    assert(invert(109, 5, 3) == 85);
}

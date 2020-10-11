/*
Write the function setbits(x, p, n, y) that returns x with the n
bits that begin at position p set to the rightmost n bits of y,
leaving the other bits unchanged.

to build: gcc -g ex_02_06.c -o ex_02_06
*/

#include <stdio.h>
#include <assert.h>

#define NUMBER unsigned char


NUMBER mask(int p, int n){
    NUMBER m = 0;
    return ~((~(~m << n)) << (p-n+1));
}

NUMBER clear_bits(NUMBER x, int p, int n){
    return x & mask(p, n);
}

NUMBER isolate_bits(NUMBER y, int p, int n){
    return y & (~mask(p, n));
}

NUMBER setbits(NUMBER x, int p, int n, NUMBER y){
    return clear_bits(x, p, n) | isolate_bits(y, p, n);
}

int main(){
    NUMBER r = setbits(125, 6, 2, 57);
    assert(r == 61);
}

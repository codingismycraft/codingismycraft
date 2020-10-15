/* In a two's complement number system, x &= (x-1) deletes the rightmost
1-bit of x. Explain why. Use this observation to write a faster implementation
of bitcount.

to build: gcc -g ex_02_09.c -o ex_02_09
 
In a two's complement number system, x &= (x-1) deletes the rightmost
1-bit of x. Explain why. Use this observation to write a faster implementation
of bitcount.
 *
A number can either be odd or even:

I. odd number
109: 01101101

if we subtract from it 1 we are getting 108 which 
in decimal is: 
108: 01101100

so 109 & 108 = 01101100

II. even number
116: 01110100

if we subtract from it 1 we are getting 115 which 
in decimal is: 
115: 01110011

Note that the all the bits after 116's right most bit
are reverted so 116 & 115 will give 01110000 which is
has the rightmost bit deleted.

to build: gcc -g ex_02_09.c -o ex_02_09
*/
#include <stdio.h>
#include <assert.h>


#define NUMBER unsigned char

int bitcount(NUMBER x){
    int c = 0;
    for(c = 0; x; ++c, x&= (x-1))
        ;
    return c;
}

int main(){    
    assert(bitcount(0) == 0);
    assert(bitcount(1) == 1);
    assert(bitcount(2) == 1);
    assert(bitcount(15) == 4);
    assert(bitcount(122) == 5);
    assert(bitcount(255) == 8);
}

/* Write a function `rightrot(x, n)` that returns the value of the integer
x rotated to the right by n bit positions.

to build: gcc -g ex_02_08.c -o ex_02_08

Example:
x = 10111001, n = 2 should return 01101110
or (185, 2) should return 110
*/

#include <limits.h>
#include <assert.h>

#define NUMBER unsigned char


NUMBER rightrot(NUMBER x, int n){
    const int l = sizeof(x) * CHAR_BIT;
    return (x >> n) | (x << (l-n));
}

int main(){
    assert(rightrot(185, 2) == 110);
}

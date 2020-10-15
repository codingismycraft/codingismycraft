/* Rewrite the function lowert, which converts upper case letters to
lower case, with a conditional expression instead of if-else.

to build: gcc -g ex_02_10.c -o ex_02_10
*/

#include <assert.h>

int lower(int c){
    /*
     A-Z: 65 - 90
     a-z: 97 -122
     */

    return c >= 'A' && c <= 'Z' ?  c - 'A' + 'a' : c;
}

int main(){
    assert('a' == lower('A'));
    assert('a' == lower('a'));
}

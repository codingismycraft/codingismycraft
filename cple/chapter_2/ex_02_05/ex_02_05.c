/* Write the function any(s1, s2) which returns the first location
 * in the string s1 where any character from the string s2 occurs, or
 * -1 if s1 contains no characters from s2.

 to build: gcc -g ex_02_05.c -o ex_02_05
 */

#include <assert.h>
#include <stdio.h>

int any(char s1[], char s2[]){
    int i1, i2;

    for(i1 = 0; s1[i1] != '\0'; ++i1){
        for(i2 = 0; s2[i2] != '\0'; ++i2){
            if (s1[i1] == s2[i2]){
                return i1;
            }
        }
    }
    return -1;
}


int main(){
    char s1[] = "this is a test";
    char s2[] = "kzq";
    assert(any(s1, s2) == -1);

    char s3[] = "tjalksj";
    assert(any(s1, s3) == 0);

    char s4[] = "kzqi";
    assert(any(s1, s4) == 2);
}

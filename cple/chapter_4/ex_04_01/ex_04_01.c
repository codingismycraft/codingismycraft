/* Wrire a function strrindex(s, t), which returns the position
 * of the rightmost occurance of t in s or -1 if there is none.
 *
 * to build: gcc -g ex_04_01.c -o ex_04_01
 * */

#include <assert.h>
#include <string.h>

int strrindex(char s[], char t[]){
    const int l1 = strlen(s);
    const int l2 = strlen(t);
    int i,j;

    for(i = l1; i >=l2; --i)
    {
        for(j = 0; j < l2 && t[j] == s[i+j-l2]; ++j)
            ;
        if (j == l2)
            return i - l2;
    }
    return -1;
}

int main(){
    char s[] = "abc thiaisoooois";
    char t[] = "abc";
   
    assert(strrindex(s, "is") == 14);
    assert(strrindex(s, "abc") == 0);
}


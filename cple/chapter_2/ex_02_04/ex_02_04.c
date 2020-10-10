/* Write an alternate version of squeeze(s1, s2) that deletes each
 * character in s1 that matches any character in s2.

 to build: gcc -g ex_02_04.c -o ex_02_04
 */

#include <assert.h>
#include <stdio.h>

void squeeze(char s1[], char s2[]){
    int i1, i2, j;
    j = 0;
    for(i1 = 0; s1[i1] != '\0'; ++i1){
        for(i2 = 0; s2[i2] != '\0'; ++i2){
            if (s1[i1] == s2[i2]){
                i2 = -1;
                break;
            }
        }
        if(i2 >=0)
            s1[j++] = s1[i1];
    }
    s1[j] = '\0';
}


int main(){
    char s1[] = "qthikzs kzzzzqqisqqqq a tzeqqst";
    char s2[] = "kzq";
    printf("%s\n", s1);
    squeeze(s1, s2);
    printf("%s\n", s1);
}

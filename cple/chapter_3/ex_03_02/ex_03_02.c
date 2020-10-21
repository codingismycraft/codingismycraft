/* Write a function escape(s, t) that converts characters like new line
 * and tabs into visible escape sequences like \n and \t as it copies 
 * t to s.
 *  
 * to build: gcc -g ex_03_02.c -o ex_03_02
 * */

#include <assert.h>
#include <stdio.h>

void escape(char s[], const char* t) {
    int i=0, j=0, c = 0;
    while( (c = t[i++]) != '\0'){
        switch (c) {
            case '\n':
                s[j++] = '\\';
                s[j++] = 'n';     
                break;
            case '\t':
                s[j++] = '\\';
                s[j++] = 't';     
                break;
            default:
                s[j++] = c; 
                break;
        }
    }
    s[j] = '\0';
}

void unescape(char s[], const char* t) {
    int i=0, j=0, c = 0;
    while( (c = t[i++]) != '\0'){
        if (c != '\\')                
            s[j++] = c; 
        else {
                switch (t[i]) {
                    case 'n':
                        s[j++] = '\n'; 
                        i++;
                        break;
                    case 't':
                        s[j++] = '\t'; 
                        i++;
                        break;
                    default:
                        s[j++] = c; 
                        break;
                }
        }
    }
    s[j] = '\0';
}

int main(){
    char s1[1000];
    char s2[1000];
    const char* t = "this\tis a \ntest";
    escape(s1, t);
    printf("%s\n", t);
    printf("%s\n", s1);
    unescape(s2, s1);
    printf("%s\n", s2);
}


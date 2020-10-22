/* Write a function expand(s1,s2) that expands shorthand 
 * notations like a-z in the string s1 into the equivalent 
 * complete list abc…xyz in s2. Allow for letters of either 
 * case and digits, and be prepared to handle cases 
 * like a-b-c and a-z0-9 and -a-z. Arrange that a leading or
 * trailing -is taken literally.
 *
 * to build: gcc -g ex_03_03.c -o ex_03_03 
 * */

#include <assert.h>
#include <stdio.h>


void expand(char s[], const char* t) {
    int i=0, c=0, j=0, previous=0, next=0;
    while( (c = t[i]) != '\0' ){
        if(c != '-' || i == 0) {
            s[j++] = t[i];
            ++i;
        }
        else {
            previous = t[i-1];
            next = t[i+1];

            if (next == '\0') {
                s[j++] = t[i];
                ++i;
            }
            else if (previous >= 'a' && previous <= 'z' &&  
                     next >= 'a' && next <= 'z'  && previous < next){
                for(c = previous+1; c < next; ++c)
                    s[j++] = c;
                i += 1;          
            }
            else if (previous >= '0' && previous <= '9' &&  
                     next >= '0' && next <= '9'  && previous < next){
                for(c = previous+1; c < next; ++c)
                    s[j++] = c;
                i += 1;          
            }
            else {
                s[j++] = t[i];
                ++i;               
            }
        }
    }
    s[j] = '\0';
}

int main(){
    char buffer[1000];

    char* strgs [] = {
        "",
        "-",
        "-a-",
        "-a-z-aasas-z",
        "a-z",
        "-a-z-",
        "-",
        "--",
        "-a-1",
        "-a-1-9",
        "-a-1-9----",
        "-a-b-c",
        '\0'
    };

    int index = 0;

    while (strgs[index]){
        printf("\"%s\" :", strgs[index]);
        expand(buffer, strgs[index]);
        printf("\t%s\n", buffer);
        ++index;
    }
}



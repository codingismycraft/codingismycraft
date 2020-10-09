/*Write a loop equivalent to the for loop above without using && or ||.

to build: gcc -g ex_02_02.c -o ex_02_02
to test: cat text | ex_02_02 or
cat test1.c | ex_02_02
 */

#include <stdio.h>

#define MAX_LINE 1000

char line[MAX_LINE];
char max_line[MAX_LINE];

enum special_chars {
    end_of_string = '\0',
    new_line = '\n'
};

int max_length = 0;
int readline();

int main(){
    while (readline() > 0);
    printf("%s\n",max_line);
    printf("%i\n",max_length);
}

int readline(){
    int c;
    int length = 0;
    int i;

    while(length < MAX_LINE-1){
        c = getchar();
        if (c == EOF)
            break;
        else
            line[length++]=c;

        if (c == new_line)
            break;
    }
    line[length] = end_of_string;

    if(length > max_length){
        for(i=0; i < length; ++i)
            max_line[i] = line[i];
       max_length = length;
    }

    return length;
}
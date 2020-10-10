/* Write the function htoi(s) which converts a string of hexadecimal
 * digits (including an optional 0x or 0X) into its equivalent integer
 * value.  The allowable digits are 0 .. 9, a ..f and A..F.

to build: gcc -g ex_02_03.c -o ex_02_03
 */

#include <assert.h>
#include <stdio.h>

int htoi(char s[]){
    int pos = 0;
    int digit_value;
    int value = 0;
    int l =0;

    if (s[pos] == '0'){
        pos++;
        if(s[pos] == 'x' || s[pos] == 'X') {
            pos++;
        }
    }

    while(s[pos] != '\0'){
        if (s[pos] >= '0' && s[pos] <= '9')
            digit_value = s[pos] - '0';
        else if (s[pos] >= 'a' && s[pos] <= 'f')
            digit_value = s[pos] - 'a' + 10;
        else if (s[pos] >= 'A' && s[pos] <= 'F')
            digit_value = s[pos] - 'A' + 10;
        else
            assert(0);

        value = 16 * value +  digit_value;
        l++;
        pos++;
    }

    return value;
}

int main(){
    char s1[] = "cbfe";
    assert(52222 == htoi(s1));

    char s2[] = "0x4faf62";
    assert(5222242 == htoi(s2));
}

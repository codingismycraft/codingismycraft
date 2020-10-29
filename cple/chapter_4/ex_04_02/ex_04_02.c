/* Extend atof to handle scientific notation of the form
 *
 *  123.45e-6
 *
 * where floating-point number may be followed by e or E and
 * an optionaly signed exponent.
 *
 * to build: gcc -g ex_04_02.c -o ex_04_02
 * */

#include <ctype.h>
#include <stdio.h>


double atof(char s[]){
    int i=0, c=0, sign=1;
    double v = 0.0;
    int decimal_factor = 1;
    int in_decimal_part = 0;
    int scientific_factor = 0;
    int scientific_factor_sign = 1;

    while(isspace(s[i])) ++i;

    if (s[i] == '+'){
        sign = 1;
        i++;
    }
    else if (s[i] == '-'){
        sign = -1;
        i++;
    }

    while( (c = s[i]) != '\0'){
        if(isdigit(c)){
            v = v * 10 + c - '0';
            if(in_decimal_part)
                decimal_factor *= 10;
        }        
        else if (c == '.') 
            in_decimal_part = 1;
        ++i;

        if (s[i] == 'e' || s[i] == 'E') {
            i++;
            
            if (s[i] == '+'){
                scientific_factor_sign = 1;
                i++;
            }
            else if (s[i] == '-'){
                scientific_factor_sign = -1;
                i++;
            }

            while( (c=s[i]) != '\0'){
                scientific_factor = (scientific_factor * 10 + c - '0');            
                ++i;
            }
        }
    }

    double exp = 1;

    while(scientific_factor--)
        exp *= 10;

    if (scientific_factor_sign == -1)
        exp = 1 / exp;
    
    v /= (sign* decimal_factor);

    return v * exp;
}

int main(){
    char s[] = "-123122.91e2";
    printf("%f\n", atof(s));
}


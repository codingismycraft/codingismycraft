/* Write a program to convert Fahrenheit to Celsius.

to build: gcc ex_01_15.c -o ex_01_15
*/
#include <assert.h>
#include <stdio.h>

#define INSIDE_A_WORD 1
#define OUTSIDE_A_WORD 0
#define MAX_LENGTH 15

int fahr3celsius(int fahr_degrees){
    return (fahr_degrees - 32) * 5 / 9;
}

int main() {
    int fahr_degrees;
    for(fahr_degrees=0; fahr_degrees <= 300; fahr_degrees+=20)
    {
        printf("%3i %3i\n", fahr_degrees, fahr3celsius(fahr_degrees));
    }
}

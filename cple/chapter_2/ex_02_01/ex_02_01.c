/* Write a program to determine the sizes of char, short, int
 * and long variables both signed and unsigned by printing
 * appropriate values from standard headers and by direct
 * computation.
 * 
 * Implementation details
 * =======================
 * The easy way to find the sizes is simply by using the limits 
 * header file which exposes them as constants.
 * 
 * Another way to compute the sizes is using bitwise manipulations; given
 * an integral type T, its maximum value should be ~0.
 * 
 * 
*/

#include <stdio.h>
#include <limits.h>
#include <float.h>

void bin(signed char n) 
{ 
    /* step 1 */
    if (n > 1) 
        bin(n/2); 
  
    /* step 2 */
    printf("%d", n % 2); 
} 

int main(){
    printf("signed char %i to %i \n", SCHAR_MIN, SCHAR_MAX);
    printf("unsigned char %i to %i \n", 0, UCHAR_MAX);
    
    printf("signed int %i to %i \n", INT_MIN, INT_MAX);
    printf("unsigned int  %d to %u \n", 0, UINT_MAX);
    
    printf("signed short %i to %i \n", SHRT_MIN, SHRT_MAX);
    printf("unsigned short  %i to %i \n", 0, USHRT_MAX);
    
    printf("signed long %ld to %ld \n", LONG_MIN, LONG_MAX);
    printf("unsigned long %lu to %lu \n", 0, ULONG_MAX);
    
    return 0;
}


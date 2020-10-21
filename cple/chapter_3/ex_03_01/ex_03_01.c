/* Our binary search makes two tests inside the loop, when one
 * would suffice. Write a version with only one test inside the 
 * loop and measure the difference in run-time.
 *
 * to build: gcc -g ex_03_01.c -o ex_03_01
 * */

#include <assert.h>
#include <stdio.h>

int binsearch(int x, int v[], int n) {
    int low = 0, high = n - 1, mid = (low + (high - low)) / 2;
    while(high >= low && v[mid] != x){
        if (v[mid] > x)
            high = mid - 1;
        else
            low = mid + 1;
        mid = low + (high - low) / 2;    
    }
    return v[mid] == x ? mid : -1;    
}

int main(){
    int v[] = { 1, 10, 12, 14, 19, 20, 22 };

    assert(binsearch(1, v, 7) == 0); 
    assert(binsearch(10, v, 7) == 1); 
    assert(binsearch(12, v, 7) == 2); 
    assert(binsearch(14, v, 7) == 3); 
    assert(binsearch(19, v, 7) == 4); 
    assert(binsearch(20, v, 7) == 5); 
    assert(binsearch(22, v, 7) == 6);

    assert(binsearch(3, v, 7) == -1); 
    assert(binsearch(0, v, 7) == -1); 
    assert(binsearch(21, v, 7) == -1); 
    assert(binsearch(23, v, 7) == -1); 
}

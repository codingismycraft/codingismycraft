// A program to count blanks, tabs and newlines.
// to build: gcc ex_01_08.c -o ex
// to test: cat ex_01_08.c | ex
#include <stdio.h>

int main() {
    int c;

    int blanks, tabs, newlines;
    blanks = tabs = newlines = 0;

    while ( (c = getchar()) != EOF) {
        if (c ==' ')
            blanks +=1;
        else if (c =='\t')
            tabs += 1;
        else if (c =='\n')
            newlines += 1;
    }

    printf("Blanks: %d\n", blanks);
    printf("Tabs: %d\n", tabs);
    printf("newlines: %d\n", newlines);
}

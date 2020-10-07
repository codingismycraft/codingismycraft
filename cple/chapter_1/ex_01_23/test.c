/* This is a junk program meant to be used as the input to ex_01_23

Before running the test you can confirm the validity of by:

gcc test.c -o junk
*/


// This should be omitted.
// /* junk = 'asdad'

void main(){

    int i =0; // This should be omitted.
    char* s1 = " This // should be visible.";
    char* s2 = " This /* should be visible.";
    char* s3 = "abc\"junk"; /* This should

        be ommited! */



    char* s4 = "abc"; /* This should
        be ommited!
    */

    int j, k;
    j/* this should be ommited */ =k /* this should be ommited */  =0; // junk
    k =1;
    i = j / k;
}
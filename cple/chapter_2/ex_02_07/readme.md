_Write a function `invert(x, p, n)` that returns x with the n
bits that begin at position p inverted (i.e. changed into 0 and
vice versa), leaving the others unchanged._

Example

For the following parameters:
```
    x = 109 (0110:1101) p = 5 n =3
```
 
The answer must be:
```
    0101:0101 (85)
```
    
Based on the following logic:

```
    Count 5 + 1 =6 bits starting from right to left
    (the position is 0 based)

       01:101101

     From the found bit count 3 bits from left to right:
         01:101:101

     The bits that must be inverted are those
     who are enclosed by the ":" which are 101 and
     must become 010:

     0101:0101 (85) which is the answer
```

The algorithm

1. Construct a value having all of its bits set to 1
```
    unsigned char y = ~0;
    
    in binary y is 11111111    
``` 
2.  Add n zeros to the end of y:
```
    y  = y << n;
    Since in our example n is 3:
    y = y << 3;
    in binary y is 11111000
```                
    
3. Now, revert the bits of y:
```
    y = ~y;
    in binary y is 00000111
```
    
4. The position of the n bits that we want to revert in x
start at p + 1, so in order to move there the last n bits
of y we can shift to left the y by p + 1 - n:
```
    y = y << (p + 1 -n);
    Since in our example n is 3 and p is 5 the last 3 bits
    must move to the third position:
    y = y << (5 + 1 - 3);
    in binary y is  00111000     
```
 
5. At this point we are having two variables:
```
    x = 0110:1101
    y = 0011:1000
``` 
it is useful to break each value in three parts as can
be seen here:
```
    x = 01:101:101
    y = 00:111:000 
```
 
6. Note that the second group holds the bits that we want to
flip which in y are all set to 1 while all of its other 
bits are set to 0.

At this point you have to think that if a bit is set in x (1)
and unset in y (0) or unset in both the operation x ^ y 
will always give the value of x:
```
    1 ^ 0 -> 1
    0 ^ 0 -> 0
```

on the other hand is a bit is unset in x (0)
and also set in y (1) or set in both the operation x ^ y 
will always flip of x:
```
    1 ^ 1 -> 0
    0 ^ 1 -> 1
```

So, based on this property of the XOR we can now calculate
the answer to the problem:
```
    y = x ^ y;
    
    or
    
    01101101 ^ 00111000 = 01010101
```

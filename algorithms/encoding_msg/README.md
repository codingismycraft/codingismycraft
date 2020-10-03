### Description of the problem
Each letter of the alphabet is represented by its 1 based index as follows:

```
a ->  1   b ->  2   c ->  3   d ->  4   
e ->  5   f ->  6   g ->  7   h ->  8   
i ->  9   j -> 10   k -> 11   l -> 12   
m -> 13   n -> 14   o -> 15   p -> 16   
q -> 17   r -> 18   s -> 19   t -> 20   
u -> 21   v -> 22   w -> 23   x -> 24   
y -> 25   z -> 26   
```

Using the above map a sequence of numeric values like for example:

'12' can be decrypted either as 'ab' or 'l':

The objective of the exercise is to write a function that receives a numeric
sequence and returns the count of the possible strings that correspond to it.
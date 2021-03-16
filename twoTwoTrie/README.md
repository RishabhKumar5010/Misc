This is my attempt on a practice question at hackerrank:

## [Question](https://www.hackerrank.com/challenges/two-two/problem)

### Two Two

Prof. Twotwo as the name suggests is very fond powers of 2. Moreover he also has special affinity to number 800. He is known for carrying quirky experiments on powers of 2.

One day he played a game in his class. He brought some number plates on each of which a digit from 0 to 9 is written. He made students stand in a row and gave a number plate to each of the student. Now turn by turn, he called for some students who are standing continuously in the row say from index i to index j (i<=j) and asked them to find their strength.

The strength of the group of students from i to j is defined as:

```
strength(i , j)
{
    if a[i] = 0
        return 0; //If first child has value 0 in the group, strength of group is zero
    value = 0;
    for k from i to j
        value = value*10 + a[k]
    return value;
} 
```

Prof called for all possible combinations of i and j and noted down the strength of each group. Now being interested in powers of 2, he wants to find out how many strengths are powers of two. Now its your responsibility to get the answer for prof.

## My solution:

My solution is in python language.

This was my third approach/attempt to the problem, after first two getting rejected due to time-limit.

* The first approach was rudamentary checking for substring using 2 nested loops **O(n<sup>2</sup>)**. It still had my touch of optimisation, so when this got rejected it was a bit surprising. (But not so much when I saw the size of the test strings were **10<sup>5</sup>**)

* In my second approach, I made a table sort of data structure to keep track of the powers of 2, and managed to bring the time-complexity to something around **O(n x m x k)**  (**m** is the size of powers of 2 array (800 in the question), k is the number of bottleneck operations).

* In my third approach I used **trie** data structure, to store the powers of 2, did a reverse search, and also added a mechanism to store the result from previous user input (as later-on I found out that some strings were repeated in a test-case). Time complexity for this solution is **O(n x m)**

**Highlights**
* The best thing about this solution is that it is quite simple to understand and quite fast to implement..
* Some problem specific optimisations were performed, over vanilla trie.


Execution on sample text file provided (size of strings (n): 1000)

>Powers of 2, substring count in input order:\
464\
407\
447\
426\
433\
458\
445\
483\
435\
484


Execution on custom user input:

>Enter number of testcases : 1\
128232

Output:

>Powers of 2, substring count in input order:\
7



Explaination of the output:

The size of the input string (n) considered here is just 6 for this simulation, {In reality, the world is going to be very harsh on your code maybe 10<sup>5</sup> times or even more..!}

The 7 substrings that the program points to are:

```
* `1`   x 1  pow(2,0)     +1
* `2`   x 3  pow(2,1)     +3
* `8`   x 1  pow(2,3)     +1
* `32`  x 1  pow(2,5)     +1
* `128` x 1  pow(2,7)     +1
                        ------
                           7
```                           
                                 
An improved version of trie called Aho-Corasick algorithm will have a much better performance in this problem statement.\
I tested one such implementation in python, but that code needed more optimisation to show any significant improvement.\
Such algorithms are better implemented in C/C++ etc, but their development time complexity is more (pun intended), so I usually prefer python as my go to weapon. But when situation demands, C/C++ are there to save the day.\
This was not one of them. Fhew..!!

### Credits

* Thanks to [Amit Pandey](https://www.hackerrank.com/profile/amititkgp), for creating this problem statement on [hackerrank](https://www.hackerrank.com)

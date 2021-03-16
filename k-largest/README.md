## Kth Largest Element

This cpp code finds Kth Largest Element **without sorting** the given numeric array.

### Time Complexity :  O ( k.n )

### Inspiration

While checking out my mails I found this Quora Suggested Spaces article saying

*"Can you find Kth Largest Element in an array without sorting the whole array?"*

https://qr.ae/pNqkqC

It didn't took a sec to grab my attention, cause previously I have done this problem. But I did it in python where I could just pop off the element
that I already looked at to be the current maximum. And then eventually I find in the kth iteration the largest element in it.\
Now in the above article the problem is  done in cpp, so I would try the same.\
In core cpp without importing vectors and other headers, its requires additional efforts to remove the element from the array.\
Also if the array is big and the array data is to be preserved, poping of elements would require two copies of the array, which may then lead
to memory optimisation problems.

In the quora article the problem is handled by use of a quick sort logic, with just some iterations, and some swaps the kth largest element reaches kth position 
in the array. Cool!!.\
But, It still requires one to create two copies of the array, if data and order of the original array is to be preserved. \
There are other methods using min and max heap whose time complexities are in order of **O(n + kLogn)** , but they too need 2 instances of array.

https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

Now these approaches are great for time complexity of a computer, but not so much for time a human would take to understand these approaches.
**Also these algorithms are not optimised for repeatating elements.**

So I came up with this approach, which is more intuitive, and probably how a human would intuitively do this problem with a pen-paper.


### How it Works?

This algo takes the array,\
and **for k** iterations finds out the largest maximum for that iteration, which is less than the previous maximum.\
Get it??\
[ 10 , 4 , 8 , 10 , 11 , 12]
so lets say in 1st iteration maximum is found to be 12.\
in the next iteration this 12 will be remembered and next maximum 11 would be found which is less than previous max 12.

Now to find maximum in unsorted array the best and most reliable way is our trusty linear search and compare.\
which would take **n** iterations.

And so, the **time complexity of O(k.n) in worst case**. \
Now comes the repeatation optimisation.\
After finding max element in an iteration of **k iterations** (in the first for loop), the algorithm checks for the number of occurances\
of the max element, and increments the loop iterator those many times, so it saves all those repeatating iterations.
This results to :

### Best case : O(n)

i.e.

arr = [ 10 , 10 , 9 ,10 ,8 ,7 ,10]

suppose we were to find 3rd largest element.

the algorithm in the first iteration would find 10 to be largest element for that iteration.

Then it would check no. of occurances of 10 which would turn out to be 4, it would increment iterator on 0 (first iteration)\
to 4 (5th iteration); but we were supposed to do only k, i.e. 3 iteration, so loop would terminate and the result would be 10.


### Conclusion

This is a short simple algorithm to understand, alter, upgrade or copy-paste in your code.

**It calculates, the kth largest element in an array without creating a new instance of the array, and is quite optimised for repeating elements**

This code's performance in itself could be improved further, by using a linked list to store the array\
and merging the repeatation optimisation step right into the inner loop.


### Credits

* Thanks to *Proff. Madhuri Badole* (my Data Structure teacher).
* Thanks to *Mayank Sharma* (the creator of the Quora Thread).

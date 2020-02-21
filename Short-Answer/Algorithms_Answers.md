#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
 For this, the run time will be `O(n)` because as the size of the input increases, the runtime will grow at the same rate


b)
The run time will be `O(n^2)` because as the input increases, the runtime will grow at a faster rate, this is as a result of having two nested loops. The first loop runs `n` times and the second runs `n-1` times and when you multiply them together it becomes `0(n^2)`

c)
The runtime will be `O(n)` because as the size increases, the runtime will grow at the same rate, this is because the code is recurive which creates a loop that runs until n = 0
## Exercise II

When an egg is thrown from the middle floor that is `n/2` of the story building, if the eggs gets broken eliminate all the floors above it and if it doesn't get broken eliminate all the floors below it. Repeat this process until f is determined.
This is basically a binary search and the runtime complexity is 
`O(log n)`



'''
Write a function fib(n) that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence.

The 0th number of the sequence is 0.
The 1th number of the sequence is 1.

To generate the next number of the sequence, we sum the previous two.

n:      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 24, ...
'''


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(fibonacci(40))

'''
Write a function fib(n) that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence.

The 0th number of the sequence is 0.
The 1th number of the sequence is 1.

To generate the next number of the sequence, we sum the previous two.

n:      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 24, ...
'''


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, len(table)):
        table[i] = table[i - 1] + table[i - 2]

    return table[-1]


print(fibonacci(8))

'''
0th Fibonacci number is 0
1st Fibonacci number is 1

2nd F is 0 + 1 = 1
3rd = 1st + 2nd  -- 1 + 1 = 2

0 1 1 2 3 5 8 ...


Base cases

n == 0 
n == 1

Recursive case

n = fib(n - 1) + fib(n - 2)

'''

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

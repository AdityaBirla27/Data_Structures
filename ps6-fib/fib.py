#!/usr/bin/python

def fib_recursive(n):
   if n <= 1:
       return n #final return statement
   else:
       return(fib_recursive(n-1) + fib_recursive(n-2)) #recursion return to make the code run in loop

def fib_memoize(n):
    if n == 0: #return 0 when 0
        return(0)
    if n == 1:#return 1 when 1
        return(1)
    dp = [0] * (n + 1)# create empty dp array
    # find patterns
    dp[0] = 0
    dp[1] = 1
    # dp[2] = dp[1] + dp[0]
    # dp[i] = dp[i-1] + dp[i-2]->Loop should look like this based on various values of i
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return(dp[n])

def fib_bottom_up(n):
    #Base Cases
    if n == 0:#return 0 when 0
        return 0
    elif (n == 1) or (n == 2):#return 1 when 1 or 2
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    #Just like previous question
    # dp[3] = dp[2] + dp[1]
    # dp[i] = dp[i-1] + dp[i-2]->Loop should look like this based on various values of i
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

def fib_in_place(n):
    fib_gen = fib()
    for _ in range(n):
        next(fib_gen)#To save memory
    return next(fib_gen)

def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

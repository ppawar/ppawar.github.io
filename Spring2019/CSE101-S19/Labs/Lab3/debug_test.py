def square (n):
    sq = 0
    for i in list(range(n)):
        sq = sq + n            # set breakpoint on this line
    return sq

def sumOfSquares (n):
    s1 = square(n)     # set breakpoint on this line
    s2 = square(n)     # set breakpoint on this line
    return s1 + s2

def sumOfSumOfSquares (x, y):
    sos1 = sumOfSquares(x)        # set breakpoint on this line
    sos2 = sumOfSquares(y)        # set breakpoint on this line
    return sos1 + sos2            # set breakpoint on this line

def main ():
    n = 1
    result = sumOfSumOfSquares(n, 3)  # set breakpoint on this line
    print('Result is ' + str(result)) # set breakpoint on this line

main()

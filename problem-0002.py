# Define a generator of the fibonacci sequence; want to evaluate this in lazy and space efficient fashion
def fib(n):
    last = 0
    penult = 0
    current = 0
    counter = 1
    while counter <= n:
        if counter > 1:
            penult = last
            last = current
            current = last + penult
        else:
            current = 1
        yield current
        counter += 1

evenSum = 0
for fibNum in fib(4000000):
    if fibNum > 4000000:
        break
    elif fibNum % 2 == 0:
        evenSum += fibNum
print evenSum
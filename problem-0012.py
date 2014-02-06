import math

# Prime number generator
def prime(n):
    counter = 1
    primes = []
    candidate = 2
    while counter <= n:
        hasDivisor = False
        for prime in primes:
            hasDivisor = (candidate % prime == 0)
            if hasDivisor or prime > candidate**(.5):
                break
        if not hasDivisor:
            counter += 1
            primes.append(candidate)
            yield candidate
        candidate += 1

# Get the list of the first five hundred primes for the purposes of this exercise
primes = []
for p in prime(500):
    primes.append(p);
divisors = {}

# Now use this information for calculating the number of divisors for a given number
def numDivisors(n):

    # Return cached copy if it exists
    if n in divisors:
        return divisors[n]
    
    # Otherwise compute the number of divisors from the prime factorization of the number
    counter = 0
    primeFactorPowers = []
    unExplained = n
    for i in range(0, len(primes)):
        if(unExplained == 1):
            break
        exponent = 0
        candidate = 1
        while unExplained % (candidate*primes[i]) == 0:
            candidate *= primes[i]
            exponent += 1
        primeFactorPowers.append(exponent)
        unExplained /= candidate
    numDivisors = 1
    for primeFactorPower in primeFactorPowers:
        numDivisors *= (primeFactorPower+1)
    divisors[n] = numDivisors
    return numDivisors

# for i in range(1,20):
#     print "Number evaluated is {0}, Number of Divisors is {1}".format(i, numDivisors(i))

for i in range(2,100000):
    # print "Here"
    latestIndex = i
    latestNum = int(math.floor(i/float(2))*2+1)*int(math.ceil(i/float(2)))
    print latestIndex, latestNum
    # Formula for i-th triangle number - note that these two factors have completely different sets of divisors
    latestNumDivisors = numDivisors(int(math.floor(i/float(2))*2+1))*numDivisors(int(math.ceil(i/float(2))))
    print "Considering {0}-th triangle nubmer. Value is {1}. Number of divisors is {2}".format(latestIndex, latestNum, latestNumDivisors)
    if latestNumDivisors >= 500:
        break

# print latestNum
# print latestNumDivisors



# # Formula for the triangle numbers
# def triangleNum(n):
#     for i in range(1, n+1):
#         yield int((math.floor(i/float(2))*2+1)*math.ceil(i/float(2)))

# # The two component pieces here never have any common divisor greater than one
# # So we can multiply the number of factors on the right side by the number on the left side

# # Now there might be something interesting algebraic going on 


# def triangleNumasdf asd 



# for i in triangleNum(10):
#     print i
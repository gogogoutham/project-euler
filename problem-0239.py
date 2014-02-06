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


# Get the list of all the primes less than one million
limit = 100
primes = []
for p in prime(limit):
    if p > limit:
        break
    primes.append(p)

numDisplaced = 22
numTotal = len(primes)

probSingleDisplacedSet = (math.factorial(limit - numTotal + numDisplaced))/float(math.factorial(limit))
for i in range(1, numDisplaced+1):
    probSingleDisplacedSet += (pow(-1,i) * 
    float(math.factorial(numDisplaced))/(math.factorial(numDisplaced-i)*math.factorial(i)) *
    float(math.factorial(limit-numTotal+numDisplaced-i))) / float(math.factorial(limit))


probAllDisplacedSets = probSingleDisplacedSet*math.factorial(numTotal)/(math.factorial(numDisplaced)*math.factorial(numTotal - numDisplaced))
print probAllDisplacedSets
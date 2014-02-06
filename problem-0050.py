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

# Given a list of consecutive primes and the index of particular prime, returns the longest consecutive sum of smaller primes equal to that prime (if such a sum exists)
def longestPrimeConsecSum (i, primes):
    partialSum = 0
    firstIndex = 0
    lastIndex = 0
    for j in range(0, i):
        lastIndex = j
        partialSum += primes[lastIndex]
        if partialSum > primes[i]:
            break
        elif partialSum == primes[i]:
            return [firstIndex, lastIndex, primes[i]]
    for k in range(1, i):
        firstIndex = k
        partialSum -= primes[k-1]
        if partialSum == primes[i]:
            return [firstIndex, lastIndex, primes[i]]
        elif partialSum < primes[i] and lastIndex < i:
            lastIndex += 1
            partialSum += primes[lastIndex]
        # if lastIndex < i:
        #     lastIndex += 1
        #     partialSum += primes[lastIndex]
    return [False, False, primes[i]]


# Get the list of all the primes less than one million
limit = 1000000
maxRange = 0
maxRangeInfo = False
primes = []
for p in prime(limit):
    if p > limit:
        break
    primes.append(p)
    rangeInfo = longestPrimeConsecSum(len(primes)-1,primes)
    if isinstance(rangeInfo[0],int) and (rangeInfo[1] - rangeInfo[0] + 1) > maxRange:
        maxRangeInfo = rangeInfo
        maxRange = rangeInfo[1] - rangeInfo[0] + 1
    print rangeInfo
print "Finally, we are here:"
print maxRangeInfo, maxRange
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

numPrimes = 10001

nthPrime = 0
for primeNum in prime(numPrimes):
    nthPrime = primeNum
print primeNum
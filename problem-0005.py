# Generator for the prime number sequence
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

targetVal = 20

primes = []
for primeNum in prime(targetVal):
    if primeNum > targetVal:
        break
    primes.append(primeNum)

print primes

outputVal = 1
for prime in primes:
    reducer = targetVal
    while reducer/float(prime) > 1:
        outputVal *= prime
        reducer /= float(prime)    
    print outputVal

print outputVal
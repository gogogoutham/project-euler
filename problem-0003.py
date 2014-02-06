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

val = 600851475143
maxPrimeDivisor = 0

for primeNum in prime(val):
    print primeNum
    if val % primeNum == 0:
        maxPrimeDivisor = primeNum
    if primeNum > val**(.5):
        break

print maxPrimeDivisor
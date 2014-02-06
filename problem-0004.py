maxPal = 0

for i in range(100, 1000):
    print "Iteration {0}, Max Palindrome is {1}".format(i, maxPal)
    for j in range(i, 1000):
        prod = i*j
        if prod < maxPal:
            continue
        elif str(prod) == str(prod)[::-1]:
            maxPal = prod
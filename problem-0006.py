cap = 100
sum = 0

for i in range(1, cap+1):
    for j in range(1, cap+1):
        if i != j:
            sum += i*j

print sum
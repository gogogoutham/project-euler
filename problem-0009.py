cap = 1000

output = False

for x in range(1, cap-1):
    for y in range(1, min(x, cap-x)):
        z = cap - x - y
        # print "{0}, {1}, {2}".format(x,y,z)
        if 2*max(x**2, y**2, z**2) == x**2 + y**2 + z**2:
            output = x*y*z

print output
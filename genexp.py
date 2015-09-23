myGen = (x**2 for x in range(10) if x % 2 == 0)
# this does not pre-compute the sequence it just computes the next number while accessed

for i in myGen:
    print i

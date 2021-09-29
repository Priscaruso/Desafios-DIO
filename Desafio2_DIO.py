#enter a input value
x = int(input())

#print the first ten values of a vetor in the format N[i] = x, where the subsequent value of x
# is the double of the previous value
for i in range(10):
    print("N[%d] = %d" % (i, x))
    x = x * 2
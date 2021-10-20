#asks you to enter a positive integer value
x = int(input())

#calculates if all the integers from 1 to x are an odd number. If they are then it displays the values.
for i in range(1, x+1):
    if (i%2) == 1:
        print(i)

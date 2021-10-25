#enter the number of elements you want to display from the fibonacci sequence
n = int(input())

#the first value of the list
fib_list = [0]

#the list already has it's first value, so subtract one
n = n - 1

#the first (x1) and the second (x2) element in fib_list
x1 = 0
x2 = 1

#the next element in the sequence (x3) is the sum of the two previous ones (x1 and x2)
for i in range(n):
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    fib_list.append(x1)

#turns the elements of the list into a string and adds a space between the elements
fib_string = ' '.join(map(str, fib_list))
print(fib_string)




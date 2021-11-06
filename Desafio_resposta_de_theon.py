#enter the number of people
N = int(input())

# enter the number of times theon can be hitted
persons = list(input().split())

# the lowest value theon can be hitted
lowest = 0

# it guesses theon executioner
for i in range(N):
    if persons[i] == min(persons):
        lowest = persons[i]
        algoz = persons.index(lowest)
print(algoz + 1)

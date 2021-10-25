N = int(input())
persons = list(input().split())
lowest = 0


#for i in range(N):
#    if i == 0:
#        lowest = persons[i]
#        continue
#   if persons[i] < lowest:
#       lowest = persons[i]
#        lowest_pos = i
#print(lowest_pos + 1)


for i in range(N):
    if persons[i] == min(persons):
        lowest = persons[i]
        algoz = persons.index(lowest)

print(algoz + 1)
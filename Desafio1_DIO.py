#enter a grade from 0 to 100
nota = int(input( ))

#convert the numeric grades to the A,B,C,D and E grade format
if 0 <= nota < 1:
    print('E')
elif 1 <= nota <= 35:
    print('D')
elif 36 <= nota <= 60:
    print('C')
elif 61 <= nota <= 85:
    print('B')
elif 86 <= nota <= 100:
    print('A')

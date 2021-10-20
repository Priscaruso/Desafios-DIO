#method notas_media which calculates the grades average with two decimal places
def notas_media(x, y):
    media = (x+y)/2
    media = '%.2f' % media
    print('media =', media)

#method notas_validas which validates the grades if they are between 0 and 10. Otherwise it displays that the
#grade is invalid and asks you to enter a valid grade again.
def notas_validas():
    x = float(input())
    if 0 <= x <= 10:
        return x
    else:
        print('nota invalida')
        return notas_validas()

#defines the choice number 1 which calculates the grades average and after asks if you want to make a new
#calculus or not. It calls the methods notas_validas and notas_media defined above.
choice = 1
while choice == 1:
    j = -1
    k = -1
    while k == -1:
        k = notas_validas()
    while j == -1:
        j = notas_validas()
    notas_media(k,j)
    choice = 3
    while choice <1 or choice >2:
        choice = eval(input('novo calculo (1-sim 2-nao)\n'))

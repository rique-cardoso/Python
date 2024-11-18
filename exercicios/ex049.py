n = int(input('Quer a tabuada de qual número? '))
parada = int(input('Até quanto? '))
for c in range(0, parada+1):
    print('{} x {} = {}'.format(c, n, c * n))
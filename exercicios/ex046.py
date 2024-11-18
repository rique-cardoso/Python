import time
for c in range(10, 0, -1):
    if c <= 5:
        print('{}{:^20}{}'.format('\033[31m', c, '\033[m'))
    else:
        print('{:^20}'.format(c))
    time.sleep(1)
print('FELIZ ANO NOVOOOOOO!!!!!!!!!')
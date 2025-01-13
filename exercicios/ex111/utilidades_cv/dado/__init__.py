def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() and n > 0:
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor
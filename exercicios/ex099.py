def maior(*num):
    ordena = sorted(num)
    # print(ordena[(len(num) - 1)]) também funcionaria
    print(ordena[-1])
maior(2, 5, 3, 1)
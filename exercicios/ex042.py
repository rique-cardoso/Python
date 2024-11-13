lado_a = int(input('Lado A: '))
lado_b = int(input('Lado B: '))
lado_c = int(input('Lado C: '))

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):
    if lado_a == lado_b and lado_b == lado_c:
        print('É um triângulo equilátero.')
    elif (lado_a == lado_b and lado_a != lado_c) or (lado_b == lado_c and lado_b != lado_a) or (lado_c == lado_a and lado_c != lado_b):
        print('É um triângulo isóceles.')
    else:
        print('É um triângulo escaleno.')
else:
    print('Não é um triângulo!')
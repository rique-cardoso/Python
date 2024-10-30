lado_a = int(input('Lado A: '))
lado_b = int(input('Lado B: '))
lado_c = int(input('Lado C: '))

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):
    print('É um triângulo!')
else:
    print('Não é um triângulo!')
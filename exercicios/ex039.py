idade = int(input('Idade: '))
if idade < 18:
    print('Faltam {} anos para você realizar seu alistamento militar.'.format(18 - idade))
elif idade > 18:
    print('Passaram-se {} anos desde o seu alistamento militar'.format(idade - 18))
else:
    print('Você deve realizar o seu alistamento militar este ano.')
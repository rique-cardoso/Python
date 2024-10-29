cidade = input('Cidade: ')
is_santo = cidade.lower().find('santo')
if is_santo == 0:
    print('Essa cidade começa com SANTO')
else:
    print('Essa cidade não começa com SANTO')
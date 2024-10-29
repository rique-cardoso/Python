cidade = input('Cidade: ')
is_santo = cidade.lower().find('santo')
if is_santo == 0:
    print('Essa cidade começa com SANTO')
else:
    print('Essa cidade não começa com SANTO')
# CORREÇÃO
""" cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO') """
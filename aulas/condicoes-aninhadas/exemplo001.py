nome = input('Nome: ')
if nome == 'Henrique':
    print('Eita! Esse é o nome mais lindo que eu já vi.')
elif nome == 'Aristóteles' or nome == 'Platão' or nome == 'Sócrates':
    print('Eita! Tu é um filosófo bem importantezin, né?')
elif nome in 'Pelé Messi Neymar Cristiano Ronaldo':
    print('Eita, atrás de Eita! Tu é bom de bola, ein! Só não é melhor que eu, no meu auge.')
else: ##opcional
    print('Não me leve a mal, mas... Tu não tem nada de especial.')
print('Bom dia {}'.format(nome))
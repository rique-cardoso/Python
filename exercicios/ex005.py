""" numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('Antecessor: {}\nSucessor: {}'.format(antecessor, sucessor)) """

#CORREÇÃO:

numero = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format(numero, (numero - 1), (numero + 1)))
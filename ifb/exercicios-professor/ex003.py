""" Declare uma variável A com valor inicial 10 e uma variável B
com valor inicial 5. Utilize atribuições e quantas variáveis
desejar para permutar os valores de A e B. O seu programa
deve apresentar na tela o valor de A e o valor de B (espera-se
que estejam trocados e que contenham 5 dígitos cada). """
a = 10
b = 5
auxiliar = a
a = b
b = auxiliar
print('A:{:05}\nB:{:05}'.format(a, b))
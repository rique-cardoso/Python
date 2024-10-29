frase = input('Digite uma frase: ')
# |S|ó| |s|e|i| |q|u|e|  |n |a |d |a |  |s |e |i |
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|
ocorrencias_a = frase.upper().count('A') # -> 2
primeira_ocorrencia_a = frase.upper().find('A') # -> 12
ultima_ocorrencia_a = frase.upper().rfind('A') # -> 14
print('Número de ocorrências de A: {}\nPrimeira ocorrência de A: {}\nÚltima ocorrência de A: {}'.format(ocorrencias_a, primeira_ocorrencia_a, ultima_ocorrencia_a))
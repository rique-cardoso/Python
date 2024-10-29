nome = input('Nome completo: ')
# |H|e|n|r|i|q|u|e| |P|r |a |t |e |s |  |C |a |r |d |o |s |o |
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|
maiusculas = nome.upper() # -> HENRIQUE PRATES CARDOSO
minusculas = nome.lower() # -> henrique prates cardoso
tamanho_sem_espacos = len(nome.replace(' ', '')) # -> 21
tamanho_primeiro_nome = len(nome.split()[0]) # -> 8
print('Maiúsculas: {}\nMinúsculas: {}\nTamanho sem espaços: {}\nTamanho primeiro nome: {}'.format(maiusculas, minusculas, tamanho_sem_espacos, tamanho_primeiro_nome))
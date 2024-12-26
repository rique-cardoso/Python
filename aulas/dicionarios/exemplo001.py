pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['idade']) # 22
# print(pessoas[0]) # vai dar erro, pois pessoa é dicionário e é acessado por sua key
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.') # O Gustavo tem 22 anos
print(pessoas.keys()) # nome, sexo, idade
print(pessoas.values()) # Gustavo, M, 22
print(pessoas.items()) # keys e values juntos
del(pessoas['sexo']) # o elemento sexo, foi apagado
pessoas['nome'] = 'Leandro' # modificou o value da key 'nome'
pessoas['peso'] = 98.5 # adicionou uma nova key com um novo valor
# Iterando Dicionários:
for key in pessoas.keys():
    print(key)
for value in pessoas.values():
    print(value)
for key, value in pessoas.items():
    print(key, value)
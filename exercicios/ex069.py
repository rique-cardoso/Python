contador_maioridade = 0
contador_homens = 0
contador_mulheres_menor20 = 0
while True:
    idade_pessoa = int(input('Idade: '))
    sexo_pessoa = input('Sexo | M, F |: ').upper()
    if idade_pessoa >= 18:
        contador_maioridade += 1
    if sexo_pessoa == 'M':
        contador_homens += 1
    if sexo_pessoa == 'F' and idade_pessoa < 20:
        contador_mulheres_menor20 += 1
    resposta_saida = input('Deseja sair? | (S,N): ').upper()
    sair = True if resposta_saida == 'S' else False
    if sair == True:
        break
print(f"""Dados Cadastrados:
      Foram cadastrados {contador_maioridade} pessoas na maioridade.
      Foram cadastrados {contador_homens} indivíduos do sexo masculino.
      Foram cadastrados {contador_mulheres_menor20} mulheres com menos de 20 anos.""")
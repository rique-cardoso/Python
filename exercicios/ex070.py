tot_gasto = produtos_mais_1000 = cont = valor_produto_mais_barato = 0
nome_produto_mais_barato = ''
while True:
    nome_produto = input('Nome do produto: ')
    preco_produto = int(input('Preço do produto: '))
    tot_gasto += preco_produto
    if preco_produto > 1000:
        produtos_mais_1000 += 1
    if cont > 0:
        if preco_produto < valor_produto_mais_barato:
            nome_produto_mais_barato = nome_produto
    else:
        nome_produto_mais_barato = nome_produto
        valor_produto_mais_barato = preco_produto
    cont += 1
    parar = input('Deseja parar? [S, N]: ').upper()
    if parar == 'S':
        break
print(f"""Produtos cadastrados com sucesso!
Total gasto: R${tot_gasto:.2f}
Produtos acima de R$1.000,00: {produtos_mais_1000}
Produto mais barato: {nome_produto_mais_barato}""")
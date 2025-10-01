from pathlib import Path

caminho = Path('exemplo001/pasta-ex001')
# caminho = Path('exemplo001') / Path('pasta-ex001') -> outra forma de fazer

print(caminho)
print(type(caminho))

for nome in ['a.txt', 'b.txt', 'c.txt', 'd.txt']:
    arquivo = caminho / nome
    print(arquivo)

print(Path.home())
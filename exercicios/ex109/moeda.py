# aumentar, diminuir, dobro, metade
def aumentar(valor, incremento, formata=False):
    valor += incremento
    if formata:
        valor = moeda(valor)
    return valor
def diminuir(valor, decremento, formata=False):
    valor -= decremento
    if formata:
        valor = moeda(valor)
    return valor
def dobro(valor, formata=False):
    valor *= 2
    if formata:
        valor = moeda(valor)
    return valor
def metade(valor, formata=False):
    valor /= 2
    if formata:
        valor = moeda(valor)
    return valor
def moeda(valor, formata=False):
    formatado = f"R${valor:.2f}"
    formatado = formatado.replace('.', ',')
    return formatado
# aumentar, diminuir, dobro, metade
def aumentar(valor, incremento):
    valor += incremento
    return valor
def diminuir(valor, decremento):
    valor -= decremento
    return valor
def dobro(valor):
    valor *= 2
    return valor
def metade(valor):
    valor /= 2
    return valor
def moeda(valor):
    formatado = f"R${valor:.2f}"
    formatado = formatado.replace('.', ',')
    return formatado
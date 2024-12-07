import math

def calcular_pontuacao(x, y):
    """Calcula a pontuação de um tiro baseado na posição (x, y)."""
    distancia = math.sqrt(x**2 + y**2)
    
    if distancia <= 1:
        return 10
    elif distancia <= 2:
        return 9
    elif distancia <= 3:
        return 8
    elif distancia <= 4:
        return 7
    elif distancia <= 5:
        return 6
    elif distancia <= 6:
        return 5
    else:
        return 0

# Entrada de dados
N = int(input(""))  # Número de tiros
pontuacao_total = 0

for _ in range(N):
    x, y = map(float, input("").split())
    pontuacao_total += calcular_pontuacao(x, y)

# Saída
print(pontuacao_total)

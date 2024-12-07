def decimal_para_mengo(numero_decimal):
    # Define os símbolos da base Mengo
    base_mengo = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "F", "L", "A", "M", "E", "N", "G", "O"]
    base = len(base_mengo)

    # Caso especial para o número 0
    if numero_decimal == 0:
        return base_mengo[0]

    resultado = ""

    # Converte para a base Mengo
    while numero_decimal > 0:
        resto = numero_decimal % base
        resultado = base_mengo[resto] + resultado
        numero_decimal //= base

    return resultado

# Entrada de múltiplos casos de teste
while True:
    try:
        numero_decimal = int(input(""))
        if numero_decimal == 0:
            break
        resultado = decimal_para_mengo(numero_decimal)
        print(f"{resultado}")
    except ValueError:
        continue
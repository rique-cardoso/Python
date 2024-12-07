dispositivos = [
    {"nome": "Pendrive", "valor": 1},
    {"nome": "Pendrive", "valor": 2},
    {"nome": "Pendrive", "valor": 4},
    {"nome": "Pendrive", "valor": 8},
    {"nome": "Pendrive", "valor": 16},
    {"nome": "Pendrive", "valor": 32},
    {"nome": "Pendrive", "valor": 64},
    {"nome": "Pendrive", "valor": 128},
    {"nome": "Unidade de Estado Sólido", "valor": 256},
    {"nome": "Unidade de Estado Sólido", "valor": 512},
    {"nome": "Disco Rígido Convencional", "valor": 1024},
    {"nome": "Disco Rígido Convencional", "valor": 2048},
    {"nome": "Disco Rígido Convencional", "valor": 4096},
    {"nome": "Disco Rígido Convencional", "valor": 8192},
]

while True:
    try:
        valor_backup = int(input(''))
        if valor_backup == 0:
            break
        if valor_backup < 0:
            continue

        dispositivos_necessarios = []
        aux = valor_backup

        while valor_backup > 0:
            for obj in reversed(dispositivos):
                if valor_backup >= obj["valor"]:
                    valor_backup -= obj["valor"]
                    dispositivos_necessarios.append(obj)
                    break

        print(f'{len(dispositivos_necessarios)}')

    except ValueError:
        continue
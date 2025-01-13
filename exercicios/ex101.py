from datetime import datetime
def voto(ano_nasc):
    idade = datetime.now().year - ano_nasc
    if idade < 16:
        return 'NEGADO.'
    elif idade < 18:
        return 'OPCIONAL.'
    elif idade >= 18:
        return 'OBRIGATÓRIO.'
ano_nasc = int(input('Ano de nascimento: '))
status_voto = voto(ano_nasc)
print(f'Seu voto é {status_voto}')
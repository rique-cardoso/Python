fitaEntrada53 = input('').upper()
fitaEntrada35 = ''
for caracter in fitaEntrada53:
    if caracter == 'A':
        fitaEntrada35 += 'T'
    elif caracter == 'T':
        fitaEntrada35 += 'A'
    elif caracter == 'C':
        fitaEntrada35 += 'G'
    elif caracter == 'G':
        fitaEntrada35 += 'C'
print(fitaEntrada35[::-1])
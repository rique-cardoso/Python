frase = 'Curso em Video Python'

#|C|u|r|s|o| |e|m| |V|i|d|e|o| |P|y|t|h|o|n|          ---          String armazenada em frase
#|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|          ---          Posições da String armazenanda em frase

# Fatiamento:

# Sintaxe -> início : fim : pula
#         -> frase[n] === caractere na posição n
#         -> frase === frase inteira

print(frase) # --> Curso em Video Python
print(frase[6]) # --> e
print(frase[6:8]) # --> em
print(frase[6:20:4]) # --> ei h
print(frase[:7]) # --> Curso e
print(frase[6::3]) # --> eVePh
print(frase[::2]) # --> Croe ie yhn

# Exibição de Textos Grandes:

print("""Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout.
sep: string inserted between values, default a space.
end: string appended after the last value, default a newline.""")
frase = 'Curso em Video Python'
frase2 = '   MySQL   '

# Frase:
#|C|u|r|s|o| |e|m| |V|i |d |e |o |  |P |y |t |h |o |n |          ---          String armazenada em frase
#|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|          ---          Posições da String armazenanda em frase

# Frase2:
#| | | |M|y|S|Q|L| | |  |
#|0|1|2|3|4|5|6|7|8|9|10|

# Métodos:

print(len(frase)) # --> 21
print(frase.count("o")) # --> 3
print(frase.find('deo')) # --> 11
print('Python' in frase) # --> true
print('Java' in frase) # --> false
print(frase.replace('Python', 'JavaScript')) # --> Curso em Video JavaScript
print(frase.upper()) # --> CURSO EM VIDEO PYTHON
print(frase.lower()) # --> curso em video python
print(frase.capitalize()) # --> Curso em video python
print(frase.title()) # --> Curso Em Video Python
print(frase2.strip()) # --> MySQL
print(frase2.rstrip()) # --> ___MySQL
print(frase2.lstrip()) # --> MySQL___
print(frase.split()) # --> ['Curso', 'em', 'Video', 'Python']
print(frase.split()[0]) # --> Curso
print('-'.join(frase)) # --> C-u-r-s-o- -em- -V-i-d-e-o- -P-y-t-h-o-n
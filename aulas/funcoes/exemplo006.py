# INTERACTIVE HELP
    # - help()
from time import sleep # é preciso importar a biblioteca para solicitá-la na help() - como no caso do sleep
help(print)
help(int)
help(sleep)
# help(math)  ===> repare que a biblioteca math não foi importada, se esta linha for executada, vai dar erro

    # - __doc__
print(input.__doc__)
lista = list()
print(lista.pop.__doc__)
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://github.com/')
except:
    print('\033[4;31mNão foi possível acessar a URL.\033[m')
else:
    print('\033[0;32mURL acessada com sucesso.\033[m')
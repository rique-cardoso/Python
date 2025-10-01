"""
C:\Users\henri\Documents\estudos-tech\Python> python
Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> from pathlib import Path
>>> Path('exemplo0021).exists()
  File "<stdin>", line 1
    Path('exemplo0021).exists()
         ^
SyntaxError: unterminated string literal (detected at line 1)
>>> Path('aulas/leitura-e-escrita-de-arquivos/exemplo002')
WindowsPath('aulas/leitura-e-escrita-de-arquivos/exemplo002')
>>> Path('aulas/leitura-e-escrita-de-arquivos/exemplo002').exists()
True
>>>     
"""

"""
 C:\Users\henri\Documents\estudos-tech\Python> python
Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> from pathlib import Path
>>> Path.cwd()
WindowsPath('C:/Users/henri/Documents/estudos-tech/Python')
>>> exit()
"""
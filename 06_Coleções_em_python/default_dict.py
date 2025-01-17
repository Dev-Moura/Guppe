"""
Módulo Collection - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionários

dicionario = {'curso': 'Programação em python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # ??? KeyError

Default Dict -> Ao crira um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em python: Essencial'

print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não.

print(dicionario)
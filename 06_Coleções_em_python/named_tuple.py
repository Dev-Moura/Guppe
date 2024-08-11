"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap tupla
tupla = (1, 2 , 3)

print(tupla[1])

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# importando

from collections import namedtuple

# Precisamos definir o nome e parâmentros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 = Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0])  # Idade
print(ray[1])  # raça
print(ray[2])  # nome

# Forma 2 - Mais usada

print(ray.idade)  # Idade
print(ray.raça)  # Raça
print(ray.nome)  # Nome

print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))

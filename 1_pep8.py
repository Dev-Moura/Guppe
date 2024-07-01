"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

zen of python

import this

A ideia da PEP8 é que possamos escrever códigos python de forma Pytônica.

[1] - Utilizar camel case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientífica:
    pass


[2] - Utilizar nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilizar 4 espaços para identação! (Configurar o tab sempre para 4 espaços)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classes com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - imports

- Imports devem ser sempre feitos em linhas separadas;

# import Errado

import sys, os

# import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imort de um mesmo pacote, recomenda-se fazer;

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de qualquer comentário
# ou docstrings e antes de constantes ou váriaveis globais.

[6] - Espaços em expressões e instruções


# Não faça:

funcao( algo [ 1 ], { outro: 2 } )

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict_['chaves'] = lista_[indice]

# Faça:

dict['chaves'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa: 5

[7] - Termine sempre uma instrução com uma nova linha em branco
"""

import this

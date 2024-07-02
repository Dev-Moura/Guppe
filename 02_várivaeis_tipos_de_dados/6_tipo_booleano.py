"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, verdadeira ou falso

True -> Verdadeiro
False -> Falso

OBS: sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

ativo = True
print(ativo)

# Operação básica:

# Negação (not):

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso oo resultado será verdadeiro. Ou seja, sempre o contrario.
"""
print(not ativo)

# OU (or):
"""
É uma operaçã binária, ou seja, depende de dois valores, ou um ou outro para ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
També é uma operaçãoo binária, ou seja, depende de dois valores, ambos os valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> false
False and False -> False
"""

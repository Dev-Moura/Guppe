"""
Tipo float

Tipo real, decimal

Casas decimais

Obs: O separados de casas decimais na programação é o ponto e não a vírgula
"""

# Errado do ponto de vista do Float, mas gera uma tupla

valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
# OBs: ao converter valores float par ainteiro, nós perdemos precisão.
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com número complexos
variavel = 5j
print(type(variavel))
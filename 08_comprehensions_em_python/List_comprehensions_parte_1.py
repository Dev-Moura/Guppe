"""
List comprehensions

- Utilizando List comprehensions ós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe da Lista Comprehensions


[dado for dado in iterável ]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10


res2 = [numero / 2 for numero in numeros]
print(res2)


def funcao(valor):
    return valor * valor


res3 = [funcao(numero) for numero in numeros]

print(res3)


# Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrado = numero * 2
    numeros_dobrados.append(numeros_dobrado)

print(numeros_dobrados)


# List comprehensions versos loop
print([numero * 2 for numero in numeros])


# Exemplo 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# Exemplo 2

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

# Exemplo 3

print([numero * 3 for numero in range(1, 10)])

# Exemplo 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
"""

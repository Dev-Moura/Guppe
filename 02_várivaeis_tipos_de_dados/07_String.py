"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # transforma em uma lista de strings


print(nome[0:4]) # slice de string

print(nome[5:14]) # Slice de string

# [ 0,       1]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])
"""
# - Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,   11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'

"""
[::-1] - COMECE DO PRIMEIRO ELEMENTO, VÁ ATÉ O ÚLTIMO ELEMENTO E INVERTA
"""

print(nome[::-1]) # Inversão de string Pythônico

print(nome.replace('e', 'i'))

print(type(nome))

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])

nome = 'ana'
print(nome)
print(nome[::-1])
"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range for para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências númericas, não de forma aleatória, mas sim de maneira especificada.
formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo forma 1
for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo 1 em 1)

#Exemplo forma 2
for num in range(4, 11):
    print(num)

forma 3
range valor_de_início, valor de parada, passo

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo forma 3
for num in range(5, 55, 5):
    print(num)

forma 4 (Inversa)

range(valor_de_ínicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

Exemplo forma 4
for num in range(10, 0, -1):
    print(num)
"""
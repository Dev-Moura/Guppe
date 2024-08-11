"""
1 - Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tea os valores lidos.

lista: list[int] = []

while len(lista) < 6:
    valor: int = int(input(f'informe o valor {len(lista) + 1}/6: '))
    lista.append(valor)

for valor in lista:
    print(valor)

=======================================================================================

2 - Faça um programa que possua uma lista denominada a que armazene 6 números inteiros.
O programa deve executar os seguintes passos:

a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) armanzene em uma variável inteira a soma entre ps valores das posições A[0], A[1] e A[5]
da lista e mostre na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.


A: list[int] = [1, 0, 5, -2, -5, 7]

soma: int = A[0] + A[1] + A[5]
print(f'A soma dos valores eh {soma}')

A[5] = 100

for valor in A:
    print(valor)

========================================================================================

3) Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos
valores para ele possui.


lista: list[int] = []
contador_pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/10: '))
    lista.append(valor)

    if valor % 2 == 0:
        contador_pares = contador_pares + 1

if contador_pares > 0:
    print(f'A lista {lista} possui {contador_pares} pares.')
else:
    print(f'A lista {lista} não possui valor pares.')

"""

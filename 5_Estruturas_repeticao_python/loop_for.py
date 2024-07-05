"""
Loop for

Loop -> Estrutura de repetição
For -> uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    Nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)


nome = 'Geek university'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10) # Temos que transforma em uma lista

# Exemplo de for 1 (iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

# range(valor_inicial, valor_final)

 OBS: O valor final não é inclusive.
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10 - não

for numero in range(1,10):
    print(numero)

Enumarete:

((0, 'G'), (1, 'e'), (3, 'k'), (4, ''), (5, 'U')...)

for indice, letra in enumarete(nome):
    print(nome[indice])

for indice, letra in enumarete(nome):
    print(letra)

for _, letra in enumarete(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transforma em uma lista

for valor in enumarate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range (1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {Soma}')

"""






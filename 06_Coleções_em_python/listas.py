"""
Lista (List)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de que são dinâmicas
e também que podemos colocar QUALQUER TIPO DE DADO.

Linguagens C/Java: Matrizes
    - ter tamanho e tipo de dados fixos;
    isto é, nessas linguagens se você criar um array inteiro com tamanho 5, esse array
    SEMPRE será do tipo inteiro e SEMPRE poderá ter no máximo 5 valores.

- Dinâmicos: Não possuem tamanho fixo: Ou seja, podemos criar a lista e simplesmente adicionar elementos:
- Qualquer tipo de dados: Não possuem um tipo de dados fixo: Em outras palavras

As listas em Python são representadas por colchetes: []

# Podemos verificar facilmente se um determinado valor está contido na lista
num = 7
for num in lista4:
    print(f'Encontrei o número {num}')
outro:
    print(f'Não encontrei o número {num}')

# Podemos classificar facilmente uma lista

lista1.sort()
print(lista1)

# Podemos contar facilmente o número de ocorrências de um valor em uma lista

imprimir(lista1.contar(1))
imprimir(lista5.count('e'))

#Adiciona elementos à lista

Para adicionar elementos ou valores a uma lista usamos a função append(), ela sempre adiciona no final da lista
NOTA: com acréscimo, só podemos adicionar 1 elemento por vez

print(lista1)
lista1.append(75)
print(lista1)

# NOTA: Com acréscimo, só podemos adicionar 1 elemento por vez
# list1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1])
print(lista1)
for [8, 3, 1] in lista1:
    print('Encontrei a lista')
outro:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como um valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
list1.insert(2,'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos reverter uma lista usando reverse()
lista1.reverso()
lista2.reverso()

print(lista1)
print(lista2)

# Ou também podemos usar este [::-1] -> slice

print(lista1[::-1])
print(lista2[::-1])

#copia uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos temos na lista
print(len(lista1))

# Podemos remover o último elemento de uma lista
# NOTA: Pop não apenas remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()

print(lista5)

# Podemos remover um elemento por índice
# NOTA: Os elementos à direita deste índice serão movidos para a esquerda.
# NOTA: Se não houver nenhum elemento inserido no índice, obteremos o erro IndexError.

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)

print(lista5)
lista5.clear()

print(lista5)

# Podemos repetir elementos de uma lista

novo = [1, 2, 3]
print(novo)

novo = novo * 3
print(novo)

Podemos facilmente converter uma string em uma lista

# Exemplo 1

curso = 'Programação Python: Essencial'
print(curso)

curso = curso.split()
print(curso)

# NOTA: Por padrão, o slipt separa os elementos da lista pelo espaço entre eles.

# Exemplo 2

course = 'Programação, em, Python, Essential'
print(curso)

curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

list6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pegue a list6, coloque espaço entre cada elemento e transforme em uma string

curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pegue a list6, coloque um cifrão entre cada elemento e transforme em uma string

curso = '$'.join(lista6)
print(curso)

lista6 = [1, 2,34, Verdadeiro, 'Geek', 'd', [1, 2,3], 45345345345]

print(lista6)
print(tipo(lista6))

# Iterando listas

# Exemplo 1

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)


# Exemplo 2 - Usando while

carrinho = []
produto = ''

while produto! = 'sair':
    print("adicionando um produto à lista ou digite 'exit' para sair: ")
    produto = entrada()
    if produto! = 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Acessamos elementos de forma indexada

# 0 1 2 3

color = ['Verde', 'Amarelo', 'Azul', 'Branco']

print(cor[0]) # Verde
print(cor[1]) # Amarelo
print(cor[2]) # Azul
print(cor[4]) # Branco

# Acessar elementos ao contrário
# Para entender melhor o índice negativo, pense na lista como uma roda
# O final de um elemento está vinculado ao início da lista

print(cor[-1]) # Branco
print(cor[-2]) # Azul
print(cor[-3]) # Amarelo
print(cor[-4]) # Verde
print(cor[-5]) # Erro, porque não há índice -5

para cores em cores:
print(cor)
índice = 0
while índice < len(cores):
    print(cores[índice])
    índice = índice + 1

# Gera índice em for

para índice, cor em enumerar(cores):
    imprimir(índice, cor)
type([])

list1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

list2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 's', 'i', 't', 'y']

list3 = []

list4 = list(range(11))

list5 = list('Geek university')


colors = ['Green', 'Yellow', 'Blue', 'White']

#  Lists accept repeated values
lists = []
lists.append(42)
lists.append(42)
lists.append(33)
lists.append(33)
lists.append(42)

print(list)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?

print(numeros.index(6))

# Em qual índice está o valor 9?

print(numeros.index(9))

# OBS: Caso não tenha esse elemento na lista, será aprensentado erro
# print(numeros.index(100))


print(numeros.index(5)) #  OBS: Retornar índice do primeiro elemento encontrado


# OBS: Se ele não encontrar o valor na lista vai retornar um erro, informando que o valor não está na lista
print(numeros.index(5,1))
# aqui estou iniciando do índice 1 em diante, a procura do valor 5


# Podemos fazer busca dentro de uma range, ou seja, qual indice começar a buscar, para procurar o valor 5

print(numeros.index(5,1)) # buscando a partir do índice 1
print(numeros.index(5,2)) # buscando a partir do índice 2
print(numeros.index(5,3)) # buscando a partir do índice 3
# print(numeros.index(5,4)) # buscando a partir do índice 4
# OBS: Caso nã tenha este elemento na lista, será apresentado erro valueError

# Podemos fazer busca dentro de um range, ínicio/fim

print(numeros.index(8, 3, 6 ))# buscar o índice do valor 8, entre 3 a 6


# Revisão de slicing

# lista[início:fim:passo]
# range[ínício:fim:passo]

# Trabalhando com slice de lista com o paramêtro 'início'

lista = [1, 2, 3, 4]
print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2]) # começa em 0, pega até o índice 2 - 1

print(lista[:4]) # começa em 0, pega até o índice 4 - 1

print(lista[1:3]) # começa em 1, pega até o índice 3 - 1

# trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2


# Invertendo valores em uma lista

nomes = ['geek', 'university']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nome = ['geek','University']

nome.reverse()
print(nome)


# soma, valor Máximo*, valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros (int) ou reais (float).

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # Máximo valor
print(min(lista))  # Mínimo valor
print(len(list))   # tamanho da lista


# Transformando uma lista em tupla

lista = [1, 2, 3 ,4 ,5 ,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3, 4]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos valueError


# copiando uma lista para outra (shallow copy e deep copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # cópia

print(nova.append(4))
print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente idependentes, ou seja, modificando uma lista, não afeta a outra. Isso em python
# é chamado de Deep Copy (cópia profunda)


# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa moficação se refletiu em ambas as listas.
# Isso em python é chamado de Shallow copy.

"""

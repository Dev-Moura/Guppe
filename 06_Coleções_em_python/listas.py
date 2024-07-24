"""
Lists

Lists in Python function as vectors/matrices (arrays) in other languages, with the difference that they are dynamic
and also that we can place ANY TYPE OF DATA.

C/Java languages: Arrays
    - have a fixed size and data type;
    that is, in these languages if you create an integer array with size 5, this array
    will ALWAYS be of type integer and can ALWAYS have a maximum of 5 values.

- Dynamic: They do not have a fixed size: In other words, we can create the list and simply add elements:
- Any data type: They do not have a fixed data type: In other words

Lists in Python are represented by square brackets: []

# We can easily check if a certain value is contained in the list
num = 7
if num in lista4:
    print(f'I found the number {num}')
else:
    print(f'I didn't find the number {num}')

# We can easily sort a list
list1.sort()
print(list1)

# We can easily count the number of occurrences of a value in a list
print(list1.count(1))
print(lista5.count('e'))

# Add elements to list

To add elements or values to a list we use the append() function, it always adds to the end of the list
NOTE: with append, we can only add 1 element at a time

print(list1)
list1.append(75)
print(list1)

# NOTE: With append, we can only add 1 element at a time
# list1.append(12, 34, 56) # Error

list1.append([8, 3, 1])
print(list1)
if [8, 3, 1] in list1:
    print('I found the list')
else:
    print('I didn't find the list')

lista1.extend([123, 44, 67]) # Place each element in the list as an additional value to the list
print(list1)

# We can insert a new element in the list by informing the index position
list1.insert(2,'New value')
print(list1)

# We can easily join two lists

list1 = list1 + list2
# list1.extend(list2)
print(list1)

# We can reverse a list using reverse()
list1.reverse()
list2.reverse()

print(list1)
print(list2)

# Or we can also use this [::-1] -> slice

print(list1[::-1])
print(list2[::-1])

# copy a list

list6 = list2.copy()
print(list6)

# We can count how many elements we have in the list
print(len(lista1))

# We can remove the last element from a list
# NOTE: Pop not only removes the last element but also returns it
print(list5)
list5.pop()
print(list5)

# We can remove an element by index
# NOTE: The elements to the right of this index will be moved to the left.
# NOTE: If there is no element in the index entered, we will get the IndexError error.

list5.pop(2)
print(list5)

# We can remove all elements (zero the list)
print(list5)
list5.clear()
print(list5)

# We can repeat elements in a list
new = [1, 2, 3]
print(new)
new = new * 3
print(new)

We can easily convert a string to a list

# Example 1

course = 'Python Programming: Essential'
print(course)
course = course.split()
print(course)
# NOTE: By default, slipt separates list elements by the space between them.

# Example 2
course = 'Programming, in, Python, Essential'
print(course)
course = course.split(',')
print(course)

# Converting a list to a string

list6 = ['Programming', 'em', 'Python', 'Essential']
print(list6)

# Below we are talking: Take the list6, put space between each element and transform it into a string
course = ' '.join(lista6)
print(course)

# Below we are talking: Take the list6, put a dollar sign between each element and transform it into a string
course = '$'.join(lista6)
print(course)


list6 = [1, 2.34, True, 'Geek', 'd', [1, 2 ,3], 45345345345]
print(list6)
print(type(list6))

# Iterating over lists

# Example 1

sum = ''
for element in list2:
    print(element)
    sum = sum + element
print(sum)


# Example 2 - Using while

cart = []
product = ''

while product != 'exit':
    print("adding a product to the list or type 'exit' to exit: ")
    product = input()
    if product != 'exit':
        cart.append(product)

for product in cart:
    print(product)

# We access elements in an indexed way

#           0         1         2       3
color = ['Gree', 'Yellow', 'Blue', 'White']

print(color[0])  # Green
print(color[1])  # Yellow
print(color[2])  # Blue
print(color[4])  # White

# Access elements in reverse
# To better understand the negative index, think of the list as a wheel
# The end of an element is linked to the beginning of the list

print(color[-1])  # White
print(color[-2])  # Blue
print(color[-3])  # Yellow
print(color[-4])  # Green
print(color[-5])  # Error, because there is no index -5

for color in colors:
    print(color)
index = 0
while index < len(colors):
    print(colors[index])
    index = index + 1

#  Generate index in for

for index, color in enumerate(colors):
    print(index, color)


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
#
# # Em qual índice está o valor 6?
#
# print(numeros.index(6))
#
# # Em qual índice está o valor 9?
#
# print(numeros.index(9))
#
# # OBS: Caso não tenha esse elemento na lista, será aprensentado erro
# # print(numeros.index(100))


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

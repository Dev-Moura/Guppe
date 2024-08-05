"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.

- Aqui no Python, os Conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjutnos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;


Conjuntos são bons para se uutilizar quando precisamos armazenanr elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erros e não fara parte do conjuntos.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elementos está contido no conjunto

if 3 in s:
    print("Temos o 3")
else:
    print("Não temos o 3")


# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionário NÃO aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário {dicionario} com {len(dicionario)} elementos')

# Conjuntos NÃO aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'conjunto: {conjunto} com {len(conjunto)} elemntos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b',True, 34.2, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com o sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# Oque você faria? Faria um loop na lista...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
conjunto = {1, 2, 3}

conjunto.add(4)
conjunto.add(4)  # Duplicidade não gera erro, Simplesmente é ignorado e não é adicionado.

print(conjunto)

# Remover elementos em um conjunto
conjunto = {1, 2, 3}
print(conjunto)

# Forma 1

conjunto.remove(3)  # NÃO É INDICE! Informamos o valor a ser removido
print(conjunto)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2

conjunto.discard(2)

print(conjunto)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro

# Forma 1 - Deep Copy

novo = conjunto.copy()
print(novo)

novo.add(4)

print(novo)
print(conjunto)

# Forma 2 - Shallow Copy

novo = conjunto

novo.add(4)

print(novo)
print(conjunto)

# Podemos remover todos os itens do conjunto

conjunto.clear()
print(conjunto)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando unior

unicos1 = estudantes_python.union(estudantes_java)
# {'Ana', 'Ellen', 'Julia', 'Marcos', 'Pedro', 'Gustavo', 'Patricia', 'Guilherme', 'Fernando'}

# unicos1 = estudantes_java.union(estudantes_python)
# {'Ellen', 'Patricia', 'Gustavo', 'Guilherme', 'Ana', 'Fernando', 'Julia', 'Pedro', 'Marcos'}
print(unicos1)

# Forma 2 - utilizando pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudante que estão em ambos os cursos

# Forma 1 - utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - utilizando o &

ambos2 = estudantes_java & estudantes_python
print(ambos2)


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso Python e um
# contendo estudantes do curso de java

# Gerar um conjunto de estudantes que não estão no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# soma*, Valor Máximo*, Valor Minímo*, Tamanho

# * Se os valores forem todos inteiros ou reais

conjunto = {1, 2, 3, 4, 5, 6}

print(sum(conjunto))
print(max(conjunto))
print(min(conjunto))
print(len(conjunto))

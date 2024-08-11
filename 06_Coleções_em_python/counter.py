"""
Módulo collections - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datatypes

Counter -> recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento


# Realizando o import

from collections import Counter


# Podemos usar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]


# Utilizando o Counter
res = Counter(lista)

print(Counter(lista))

print(type(res))

# Counter({1: 5, 2: 5, 3: 4, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


"""

from collections import Counter

# Exemplo - 3

texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget eleifend libero, quis aliquam purus.
Sed masculinos de senhora lorécia quis condimentum posuere. Vivamus blandit nec justo nec aliquam feugiat. 
Ut rutrum elit ac quam elementum viverra. Curabitur convallis ex eu lobortis pretium. 
Mauris risus neque, placerat vitae ligula nec, placerat posuere magna. Sed ut libero sollicitudin magna sagittis posuere.
Vivamus venenatis orci nibh, vitae ullamcorper enim pulvinar sit amet. Ut feugiat tellus lacinia magna fermentum bibendum.
Curabitur porttitor libero ligula, em venenatis urna blandit ac. Ut efficitur mi vitae mauris pulvinar,
nec vestibulum lacus sagittis.Sed eget est em sapien tristique iaculis. Ut vel purus suscipit, laoreet dolor nec, varius ipsum.
"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
#  Esse Counter vai contar quantas vezes uma determinada palavra foi utilizada nesse texto
# fazendo a separação da Palavra(chave):quantidadeVezesRepetida(valor)

print(res)

# Econtrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
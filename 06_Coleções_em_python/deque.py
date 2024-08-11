"""
Módulo collections Deque

Podemos dizer que o Deque é uma lista de alta performace.
"""

# Importar

from collections import deque

# Criando deques

deq = deque('Geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final

print(deq)

deq.appendleft('k')  # Adicionado no começo

print(deq)

# Remover elementos

print(deq.pop())  # remove e retorna o último elemento

print(deq)

print(deq.popleft())  # remove e retorna o primeiro item da lista

print(deq)
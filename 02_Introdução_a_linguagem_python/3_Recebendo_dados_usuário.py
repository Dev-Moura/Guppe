"""
Recebendo dados do usuário

input() ~> Todos os dados recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples ~> 'angeina jolie
- Aspas duplas ~> "angelina jolie"
- Aspas simples triplas ~> '''Angelina jolie'''
"""
# - Aspas duplas triplas ~>"""angelina jolie"""
# Entrada de dados
print("Qual seu nome? ")
nome = input() # input ~> entrada

# Exemplo de print 'antrigo' 2.x
# print('Seja bem-vindo(a) s%' % nome)

# Exemplo de print 'moderno 3.x'
# print('Seja bem-vindo{a} {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

#print("Qual sua idade? ")
#idade = input()

idade = input("Qual sua idade? ")

# Processamento

# Sáida
# Exemplo de print 'antigo' 2.x
# print('A s% tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual 3.7
print(f'A {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2024 - int(idade)}')


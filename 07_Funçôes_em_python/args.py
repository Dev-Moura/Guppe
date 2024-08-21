"""
Entendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
 chamar de qualquer coisa, desde que começe com asterisco.

 Exemplo:

 *Xis

 Mas por conveção, utilizamos *args para defini-lo


 Mas o que é *args?


 o paramêtro * agrs utilizado em uma função, coloca valores extras informando como
 entrada em uma tupla. Então desde já lembre-se que tuplas são imutaveis.


# Exemplo

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4


print(soma_todos_numeros(4, 6, 9))

# Print(soma_todos_numeros(4,6))  #TypeError

print(soma_todos_numeros(4, 6 ,9 ,5))


# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Angelina', 'gmail'))
print(soma_todos_numeros('Angelina', 'gmail', 1))
print(soma_todos_numeros('Angelina', 'gmail', 1, 2))
print(soma_todos_numeros('Angelina', 'gmail', 2, 3, 4,))
print(soma_todos_numeros('Angelina', 'gmail', 3, 4, 5, 6))

print(soma_todos_numeros('Angelina', 'gmail', 23.4, 12.5))


# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek!'
    return 'Eu não tenho certeza quem você é...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

def soma_todos_numeros(*args):
    return sum(args)

# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = (1, 2, 3, 4, 5, 6, 7)

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao pythons que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.

"""

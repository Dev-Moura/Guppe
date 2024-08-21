"""
**Kwargs

Poderiamos chmarar este parâmetro de **xix, mas por conveção chamamos de **Kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **Kwargs exige que utilizamos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.


# Exemplo

def cores_favoritas(**Kwargs):
    for pessoa, cor in Kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernada='azul', vanessa='branco' )

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')



def cumprimento_especial(**kwargs):
    if 'Geek' in kwargs and kwargs['Geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'Geek' in kwargs:
        return f"{kwargs['Geek']} Geek!"
    return 'Não tenho certeza quem você é ...'

print(cumprimento_especial())
print(cumprimento_especial(Geek='Python'))
print(cumprimento_especial(Geek='Oi'))
print(cumprimento_especial(Geek='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM):

- parâmetros obrigratórios;
- *args;
- Parâmetros default (Não obrigratórios);
- **kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, Python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# Função com a ordem incorreta de parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]
'''
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'university', 'cargo': instrutor}
'''

print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))


# Desempacotando com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'jones'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


tupla = (1, 2, 3)  # Tupla
lista = [1, 2, 3]  # Lista
conjunto = {1, 2, 3}  # dicionários


soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionario devem ser os mesmo do parâmetros da função

# dicionario = dict(d=1, e=2, f=3)  # TypeError
# soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario, lang='Python')

"""



"""
Definindo Funções

 - Funções são pequenos trechos de código que realizam tarefas específicas;
 - Pode ou não receber entradas de dados e retornar uma sáida de dados;
 - Muito uteis para executar procedimentos similares repetidas vezes;

 OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
 é bom fazer uma verificação para que a função seja simplicada.

Já utilizamos várias funções desde que iniciamos este curso:
 - print()
 - len()
 - max()
 - min()
 - Count()
 - e muitas outras;

"""
# Exemplo de utilização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do Python print()

# print(cores)

# curso = 'Programação em Python: Essencial'

# print(curso)

# cores.append('Roxo')

# curso.append('Mais dados...')   # AtributeError
# print(curso)

# cores.clear()
# print(cores)

# print(help(print))

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita o código.

# Mas então, como definir funções?
"""
Em python, a forma geral de definir função é:

def nome_da_funcao(paramentros_de_entrada):
    Bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);

parametros_de_entrada -> Opcionais, onde temos mais de um, cada um separado por vírgula, podendo ser opcionais ou não;

bloco_da_funcao -> Também chamado de corpo da função ou implementação é onde o processamento da função acontece.
Neste bloco, pode ter ou não o retorno da função

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao python que estamos definindo
uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em python para definir blocos.

"""

# Definindo a primeira função

def diz_oi():
    print("oi!")

"""
OBS: 

1 - Veja que, dentro das nossas funções podemos utilizar outras funções:
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que está função não recebe nenhum parâmetro de entrada;
4 - Veja que essa função não retornar nada;
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar o parêntese ao executar uma função.

Exemplo:

# Errado!
diz_oi

# Certo!
diz_oi()

# Errado
diz_oi ()

"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

# for cantar in range(5):
#     cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função através da variável

canta = cantar_parabens

canta()


"""
Documentando funções Docstrings

OBS: Podemos ter acesso a documentação de um função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()
"""


def diz_oi():
    """Uma função simples que retornar a string 'Oi!' """
    return 'Oi! '

def exponencial(numero, potencia=2):
    """
    Função que retornar por padrão o quadrado de 'número' ou 'número' á 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


# Exemplos

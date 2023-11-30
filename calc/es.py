"""
Módulo ES
Descrição: Este módulo provê funções de entrada e saída de dados da calculadora.
Autor: Filipe Kalikoski Coelho
Versão: 0.0.1
Data: 29/11/2023

"""


def leitora_numeros() -> list:
    """Esta função solicita entrada de dados do usuário (números a serem usados na calculadora) e armazena essa informação em uma lista."""
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"Digite o número {i+1} que deseja operar"))) 
        i+=1
    return numeros


def leitora_operacao() -> str:
    """Esta função solicita a entrada de dados do usuário (operação a ser executada) e armazena essa informação."""
    operacao = input("""Digite a operação que deseja realizar. 
Pressione + para adição; 
- para subtração; 
* para multiplicação;
/ para divisão""")
    return operacao


def leitora() -> list:
    """Essa função chama sequencialmente as funções leitora_numeros() e leitora_operacao() para solicitar entrada de dados do usuário em lógica RPN."""
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]


def escritora(resultado:float) -> None:
    """Esta função coloca o resultado na tela."""
    print(f"O resultado da operação é igual a {resultado}.")
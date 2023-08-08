# # exercício 1
#   Escreva uma função que solicite ao usuário que insira seu nome e, em seguida,
# 	armazene esse valor em uma variável. Em seguida, exiba uma mensagem de boas-vindas
# 	usando o nome digitado.

import os

def solicita_nome():
    nome_informado = input('Informe seu nome: ')
    print(f'Seja bem vindo(a) {nome_informado}!!')

# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    solicita_nome()
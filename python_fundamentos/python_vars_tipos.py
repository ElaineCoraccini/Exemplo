# Realizando importações de bibliotecas, por padrão elas serão importadas no começo
# dos arquivos .py

import os
import time # nova biblioteca para o usar o sleep

# .system serve para enviar comando para o terminal entre outras funções
# conecta e realiza os comandos no terminal(cmd)
os.system('cls') # limpa o terminal
# os.system('dir') # entra no diretório

# mostrar a versão do python:
os.system('python --version')

# taskkill serve para parar o arquivo responsavel por rodar uma aplicação ou sistema:
# os.system('taskkill /f /im chrome.exe')

# suicidio cmd:
# os.system('taskkill /f /im cmd.exe')

# Tipos de dados em Python com o tipo de dado(nao é necessario ter o tipo):
numero_inteiro_1: int = 5
numero_inteiro_2: int = 5500
numero_inteiro_3: int = 100
print(f'\nDados das variáveis do tipo int: {numero_inteiro_1}, {numero_inteiro_2}, {numero_inteiro_3}')

# variavel do tipo texto:
nome: str = 'Caue'
sobrenome: str = 'Oliveira'
texto_aleatorio: str = 'hahahhahhhaha'
print(f'\nDados das variáveis do tipo str: {nome}, {sobrenome}, {texto_aleatorio}')

# variavel do tipo float, quebrado:
salario_dev: float = 1.545
nota_aluno: float = 7.5
temperatura: float = 35.9
print(f'\nDados das variáveis do tipo float: {salario_dev}, {nota_aluno}, {temperatura}')

# Arredondando a variavel salario_dev:
print(f'\n Arredondando a variavel salario_dev: {round(salario_dev, 2)}')

# Variavel do tipo Boolean: verdadeiro ou falso:
eh_verdade: bool = True
eh_mentira: bool = False
numero_1_eh_maior_que_numero_2: bool = numero_inteiro_1 > numero_inteiro_2
print(f'\nDados das variáveis do tipo Boolean: {eh_verdade}, {eh_mentira}, {numero_1_eh_maior_que_numero_2}')

# tipo lista:
lista_de_dados: list = [
    numero_inteiro_1, # 0
    numero_inteiro_2, # 1
    numero_inteiro_3, # 2
    nome,
    sobrenome,
    texto_aleatorio,
    salario_dev,
    nota_aluno,
    temperatura,
    eh_verdade,
    eh_mentira,
    numero_1_eh_maior_que_numero_2
]
# print(f'\nDados das variáveis do tipo Lista: {lista_de_dados}')
print(f'\nMostrando o dado da posição 0 : {lista_de_dados[0]}')
print(f'\nMostrando o dado da posição 3 : {lista_de_dados[3]}')
print(f'\nMostrando o dado da posição 7 : {lista_de_dados[7]}')


# for para mostrar os itens da lista limpando o terminal antes, mas aguarda 5 segundos antes de limpar:
print('esperando...')
time.sleep(5)
os.system ('cls')
for item in lista_de_dados:
    print(item)
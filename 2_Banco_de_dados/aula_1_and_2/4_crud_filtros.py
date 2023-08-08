
import sqlite3
import os
import pandas as pd


os.system('cls')

def executar_comandos_sql(sql_string):
    """Primeira docstring: função para executar comendos SQL na base de dados usando pandas"""

    #Criando conexão com a base de dados
    conexao = sqlite3.connect('mydatabase.db')

    # Afunção do pandas chamada read_sql_query executa SQL
    #espera como parametro uma string com o SQL a ser executado
    # e a conexao com a base de dados
    retorno_do_sql = pd.read_sql_query(sql_string, conexao)

    #fechar conexão
    conexao.close()

    # Retornar os dados do query (ou seja, da busca SQL)
    return retorno_do_sql


def mostrar_opcoes(colunas_lista):
    """ Função para mostrar as opções disponíveis do programa para o usuario """

    #printar os dados usando um for na lista com as colunas disponíveis
    print('Colunas disponíveis: ')
    for indice, coluna_string in enumerate (colunas_lista):
        print(f'Coluna {indice + 1}: {coluna_string}')
    #o enumerate permite que seja possivelrodar o for com duas variáveis
    # uma sendo o indice (i) da linhae a outra sendo o valor (dado/informação)
    print()

def retornar_media_coluna(coluna_nome):
    """ Função para retornar média informada pelo usuário """

    # comando SQL
    sql_string = f'select avg({coluna_nome}) from usuarioss'
    # Executar o SQL
    retorno = executar_comandos_sql(sql_string)

    # mostrar o resultado
    print(retorno)

def contar_linhas_coluna(coluna_nome):
    """ Função para contar a coluna informada pelo usuario """

    # comando SQL
    sql_string = f'select count({coluna_nome}) from usuarioss'
    # Executar o SQL
    retorno = executar_comandos_sql(sql_string)

    # mostrar o resultado
    print('\n')
    print('LIKE: ')
    print(retorno)

def buscar_palavras_em_coluna(nome_coluna, tipo_busca, string_usuario):
    """ Função para buscar palavras chaves usando LIKE """

    # comando SQL
    string_de_busca = ''
    if tipo_busca == 'start':
        string_de_busca = f"'{string_usuario}%'"
    elif tipo_busca == 'end':
        string_de_busca = f"'%{string_usuario}'"
    elif tipo_busca == 'middle':
        string_de_busca = f"'%{string_usuario}%'"
    else:
        print('Tipo de busca é invpalido!')    
    
    
    # Executar o SQL
    sql_string = f""" 
        select + from usuarioss\
        where {nome_coluna} LIKE {string_de_busca}
    """
    # mostrar o resultado
    retorno = executar_comandos_sql(sql_string)
    print(retorno)
    
def retornar_min_e_max_coluna(coluna_nome):
    """ Função para mostrar o maior e o menor de uma coluna """

    # comando SQL
    sql_string = f'select max({coluna_nome}), min({coluna_nome}) from usuario'
    # Executar o SQL
    retorno = executar_comandos_sql(sql_string)
    print(retorno)

    # mostrar o resultado


os.system('cls')

#retornar_min_e_max_coluna('idade')

sql_retorno_colunas = 'PRAGMA table_info(usuarioss)'
colunas = executar_comandos_sql(sql_retorno_colunas)
#print(colunas)
#separando as colunas do retorno sql
colunas_lista = colunas['name'].tolist()

contador = 0

print(colunas_lista)

rodar_programa = True
while rodar_programa is True:
    mostrar_opcoes(colunas_lista)
    print('Digite s para sair\n')

    coluna_posicao = input('Informe a posição da coluna a manipular: ')

    if coluna_posicao == 's':
        break

    coluna_posicao = int(coluna_posicao)


    #validar a posição informada
    if coluna_posicao > 0 and coluna_posicao <= len(colunas_lista):
        #criar a variavel para o nome da coluna
        #extrair o nome da coluna a lista de colunas usando a posição informada
        coluna_nome = colunas_lista[coluna_posicao - 1]
        print(f'Coluna {coluna_nome} selecionada com sucesso!')

        menu_operacoes = '\n1 - media'
        menu_operacoes += '\n2 - count'
        menu_operacoes += '\n3 - busca usando LIKE'
        menu_operacoes += '\n4 - min / max'
        menu_operacoes += '\nInforme a operação: '

        operacao = int(input(menu_operacoes))

        if operacao == 1:
          #chamar funçao que retorna a média
            retornar_media_coluna(coluna_nome)
        elif operacao == 2:
            contar_linhas_coluna(coluna_nome)
        elif operacao == 3:
            #menu para o imput
            menu_input = '\n1 - start'
            menu_input += '\n2 - middle'
            menu_input += '\n3 - ebnd'
            menu_input += '\nInforme a opção: '

            tipo_busca = input(menu_input)
            
            string_usuario = input("\nInforme a string que irá para buscar no banco: ")

            buscar_palavras_em_coluna(coluna_nome, tipo_busca, string_usuario)
        elif operacao == 4:
            #retornar o menor e maior valor da coluna
            retornar_min_e_max_coluna(coluna_nome)
        else:
            print('\nFoi informado uma operação inválida!')

    else:
        print('\nInforme uma posição válida!')


#retorno = executar_comandos_sql('select * from usuarioss')
#print(retorno)
#conexao = sqlite3.connect('mydatabase.bd')
#mostrar_opcoes((['name', 'age', 'email']))
#retornar_media_coluna('nome')
#retornar_media_coluna('idade')
#buscar_palavras_em_coluna('nome', 'start', 'a')
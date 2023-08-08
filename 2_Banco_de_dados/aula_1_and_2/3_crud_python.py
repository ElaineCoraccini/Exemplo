

import sqlite3
import os

os.system('cls')

conexao = sqlite3.connect('mydatabase.db')
print('conexão criada com sucesso.')
cursor = conexao.cursor()

menu_crud = '\nEscolha uma operação abaixo: '
menu_crud += '\n1 - Selecionar'
menu_crud += '\n2 - Deletar'
menu_crud += '\n3 - Atualizar'
menu_crud += '\n4 - Inserir'
menu_crud += '\n5 - Sair'
menu_crud += '\nInforme a opção: '

#while que rodará o programa
while True:
    operacao = input(menu_crud)

    if operacao == '1':
        os.system('cls')
        cursor.execute(f'''
            SELECT * FROM usuarioss                     
        ''')
        #extrair o resultado que voltou do banco de dados

        resultados = cursor.fetchall()
        #print(resultados)
        print(type(resultados))

        for item in resultados:
            print(item)

    elif operacao == '2':
        #ler id da coluna a deletar
        id_linha = input('Informe o ID da coluna a deletar: ')
        id_linha = int(id_linha)
        os.system('cls')
        #executar o código sql
        cursor.execute(f""" 
            DELETE FROM usuarioss
            WHERE ID = {id_linha};
        """)
        #printar mensagem de sucesso quando deletar
        print(f'Linha {id_linha} excluída com sucesso!')

    elif operacao == '3':  #Atualizar
        #ler id coluna a modificar
        id_linha = input('Informe o ID da coluna a alterar: ')
        id_linha = int(id_linha)
        os.system('cls')
        


        #executar o código sql

        #printar mensagem de sucesso quando deletar

    elif operacao == '4':
        #ler dados novos
        nome_novo = input('Informe o nome do usuário: ')
        email_novo = input('Informe o e-mail do usuário: ')
        idade_nova = input('Informe a idade do usuário: ')

        os.system('cls')
        idade_nova = int(idade_nova)
        #validar dados 
        if len(nome_novo) > 3 and idade_nova > 0 and "@" in email_novo:
            cursor.execute(f"""
                UPDATE usuarios
                SET nome = '(nome_novo)', idade = {idade_nova}, email ='(email_novo)'
                WHERE id = {id_linha}
        """)
        #se válidos vamos inserir na base de dados
        print(f'Informe o nome do usuário: ')

        
    elif operacao == '5':
        print('Laço de repetição para do com sucesso!')
        break

    #Compactar nossas mudanças, para então enviar elas ao banco de dados
#conexao.commit()
#print('Comitou dados com sucesso!')
#fechar a conexão com a base de dados
#conexao.close()
#print('Conexão fechada com sucesso!')
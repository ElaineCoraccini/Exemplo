#no começo do arquivo realizamos as importações necessárias
#biblioteca sqlite serve para manipular bancos de dados do sqlite
import sqlite3
#biblioteca os que server para manipular o isitema operacional
import os

os.system('cls')

#conexao com o banco de dados
conexao = sqlite3.connect('mydatabase.db')
print('conexão criada com sucesso.')

#cursor para manipular o banco de dados
cursor = conexao.cursor()

#variável para criar tabela
nome_tabela = ''
#obs: True e False começam com maiuscula 
while True:
#ler o nome da tabela informado pelo usuario
    nome_tabela = input('Informe o nome da tabela: ')

#verificar se o nome é valido

    if nome_tabela != '' and len(nome_tabela) > 3:
        print(f'Nome {nome_tabela} é válido para tabela!')
        break
    else:
        print('Informe um nome válido!')

#Executar comandos SQL n banco de dados

cursor.execute(f''' 

    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        ID INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        email TEXT
    )

''')

print(' Tabela criada com sucesso!')

#pedir os dados ao usuario para preencher a tabela
usuario_nome = ''
usuario_idade = 0
usuario_email = ''

while True:
    #ler dados 
    #input por padrão recebe string/text
    usuario_nome = input('Informe o nome do usuario: ')
    usuario_idade = input('Informe a idade do usuário: ')
    usuario_email = input('Informe o e-mail do usuário: ')

    #converter idade para inteiro
    usuario_idade = int(usuario_idade)

    #validar os dados armazenado valores true ou false em variáveis de validação

    validacao_1 = usuario_nome != '' and len(usuario_nome) >= 3
    validacao_2 = usuario_idade > 10 and usuario_idade < 100
    validacao_3 = usuario_email != '' and "@" in usuario_email

    if validacao_1 and validacao_2 and validacao_3:
        print(f'Nome {usuario_nome}, idade {usuario_idade}, e-mail {usuario_email} são dados válidos!')
        break
    else:
        print(f'Nome é válido: {validacao_1}')
        print(f'Idade é válido: {validacao_2}')
        print(f'E-mail é válido: {validacao_3}')
        print(f'Informe dados válidos!')

# Inserir os dados na nossa base de dados
cursor.execute(f''' 
    INSERT INTO {nome_tabela} (nome, idade, email)
    VALUES ('{usuario_nome}', {usuario_idade}, '{usuario_email}')

''')

print('Dados inseridos com sucesso!')

#Compactar nossas mudanças, para então enviar elas ao banco de dados
conexao.commit()
print('Comitou dados com sucesso!')
#fechar a conexão com a base de dados
conexao.close()
print('Conexão fechada com sucesso!')
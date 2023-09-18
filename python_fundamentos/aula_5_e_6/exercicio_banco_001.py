# criar uma aplicação de gerenciamento de alunos usando SQLite3 e programação orientada a objetos (POO) em Python. 
# A aplicação permitirá criar, visualizar, atualizar e excluir registros de alunos em uma
# tabela chamada Alunos no banco de dados. Utilize a biblioteca sqlite3 para criar um banco de dados chamado escola.db.
# Crie uma tabela chamada Alunos com os seguintes campos: id, nome, idade e nota. Crie uma classe chamada Aluno.
# Crie os atributos id, nome, idade e nota na classe. Implemente o construtor __init__() para receber os valores dos atributos.
# Crie métodos de getters (get_id(), get_nome(), get_idade(), get_nota()) para acessar os valores dos atributos.
# Crie métodos de setters (set_nome(), set_idade(), set_nota()) para definir os valores dos atributos.
# Crie um método estático na classe Aluno chamado criar_aluno() que aceita os valores de nome, idade e nota como parâmetros.
# Este método deve criar uma instância da classe Aluno com os valores passados e inserir um registro na tabela Alunos com esses valores.
# Crie um método estático chamado buscar_aluno_por_id() que aceita um ID como parâmetro e retorna uma instância de Aluno com os valores
# correspondentes da tabela Alunos. Crie um método estático chamado listar_alunos() que consulta a tabela Alunos e retorna uma lista de
# instâncias de Aluno. Crie um loop principal que exibe um menu para o usuário com opções como "Criar Aluno", "Buscar Aluno por ID", "Listar Alunos"
# e "Sair". Implemente a lógica para cada opção do menu, chamando os métodos correspondentes da classe Aluno. Na opção "Criar Aluno", solicite ao
# usuário que insira nome, idade e nota e, em seguida, chame o método criar_aluno(). Na opção "Buscar Aluno por ID", peça ao usuário para inserir
# um ID e exiba os detalhes do aluno correspondente usando o método buscar_aluno_por_id(). Na opção "Listar Alunos", liste todos os alunos usando o
# método listar_alunos(). Ao sair do loop principal, feche a conexão com o banco de dados.

import sqlite3
import os

class Aluno:
    def __init__(self, id, nome, idade, nota):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Crie métodos de getters (get_id(), get_nome(), get_idade(), get_nota()) para acessar os valores dos atributos.

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_nota(self):
        return self.nota

# Crie métodos de setters (set_nome(), set_idade(), set_nota()) para definir os valores dos atributos.

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_nota(self, nota):
        self.nota = nota

# Crie um método estático na classe Aluno chamado criar_aluno() que aceita os valores de nome, idade e nota como parâmetros.
# Este método deve criar uma instância da classe Aluno com os valores passados e inserir um registro na tabela Alunos com esses valores.

    @staticmethod
    def criar_aluno(nome, idade, nota):
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        sql_string = f"""
            insert into Alunos\
            (nome, idade, nota)\
            values ('{nome}', '{idade}', '{nota}')
        """
        cursor.execute(sql_string)
        conexao.commit()
        conexao.close()
        print(f'Dados: {nome} - {idade} - {nota}', end=' ')
        print(f'inseridos na tabela Alunos com sucesso.')


# Crie um método estático chamado buscar_aluno_por_id() que aceita um ID como parâmetro e retorna uma instância de Aluno com os valores
# correspondentes da tabela Alunos. 

    @staticmethod
    def buscar_aluno_por_id (id_aluno):
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        sql_string = f"""
            select * from Alunos\
            where id = {id_aluno}
        """
        cursor.execute(sql_string)
        linha_selecionada = cursor.fetchone()
        print(linha_selecionada)
        cursor.close()
        print(f'Estes são os dados do aluno com o id {id_aluno}!')

# Crie um método estático chamado listar_alunos() que consulta a tabela Alunos e retorna uma lista de
# instâncias de Aluno.

    @staticmethod
    def listar_alunos():
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        sql_string = f"""
            select * from Alunos
        """
        cursor.execute(sql_string)
        lista_dados = cursor.fetchall()
        for linha in lista_dados:
            print(linha)
        conexao.close()
        print(f'Estes são todos os alunos cadastrados na Escola!')


def database_manager():
    os.system('cls')
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    nome_tabela = 'Alunos'
    sql_string = f''' 
            create table if not exists {nome_tabela} (\
                id integer primary key,\
                nome text(40),\
                idade integer(15),\
                nota text(3)
            )
        '''
    cursor.execute(sql_string)
    conexao.commit()
    conexao.close()

    menu_interface = '''
    1 - Criar registro de novo Aluno
    2 - Visualizar registro existente pelo ID
    3 - Visualizar todos os Alunos
    4 - Sair
    Insira a operação desejada: 
    '''

    while True:
        try:
            operacao = int(
                input(menu_interface)
            )
            # CRIAR
            if operacao == 1:
                nome = input('Informe o nome do aluno: ')
                idade = input('Informe a idade do aluno: ')
                nota = input('Informe a nota do aluno: ')

                Aluno.criar_aluno(nome, idade, nota)
            
            # VISUALIZAR POR ID
            elif operacao == 2:        
                id_aluno = input('Informe o ID do aluno que deseja visualizar os dados: ')

                Aluno.buscar_aluno_por_id(id_aluno)            

            # ATUALIZAR TODOS
            elif operacao == 3:
                Aluno.listar_alunos()

            elif operacao == 4:
                print('Você saiu. Volte sempre.')
                break

            else:
                print('Informe uma operação válida')

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    database_manager() 
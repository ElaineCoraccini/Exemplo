# 4 - Classe Funcionário:
# Crie uma classe chamada Funcionario com os atributos nome (private), salario (private) e cargo (public). Crie métodos para definir o nome
# (set_nome(novo_nome)), obter o nome (get_nome()), calcular aumento de salário (aumentar_salario(aumento)) e exibir informações completas do
# funcionário (exibir_informacoes()). Crie um construtor e trabalhe a manipulação da classe e dos dados via objetos.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.cargo = cargo

        @property
        def nome(self):
            return self.__nome
        
        @nome.setter
        def nome(self, nome_novo):
            self.__mome = nome_novo

        def aumenta_salario(self, valor_acrescimo):
            self.__salario = self.__salario + valor_acrescimo

        def exibe_informacoes(self):
            print(f'Funcionario {self._nome}, possui salário {self.__salario} e exerce cargo {self.cargo}')

if __name__ == '__main__':
    funcionario_1 = Funcionario('caue', 3000, 'dev')
    funcionario_2 = Funcionario('mr robot', 13000, 'hacker')

    print(funcionario_1.nome)
    print(funcionario_2.nome)
    funcionario_1.exibe_informacoes()
    funcionario_2.exibe_informacoes()
    funcionario_1.aumenta_salario(2000)
    funcionario_1.exibe_informacoes()
    funcionario_2.exibe_informacoes()

# nome_usuario = 'caue' snake case
# NomUsuario = 'caue' camel case

class ClasseCachorro:
    raca = 'Pastor Alemão'
    idade = 5

    def latir(latidas):
        for latida in range(latidas):
            print('au au')

    def comer(comida, horario):
        print(f'au au, comi {comida}, au au em horario {horario}')

    def mostrar_info_dog():
        print(f'O cachorro é da raça {ClasseCachorro.raca} e tem {ClasseCachorro.idade} anos')

ClasseCachorro.latir(10)
ClasseCachorro.comer('ração', '10:00 am')
ClasseCachorro.mostrar_info_dog()


class ClassePessoa:
    # atributos = variaveis
   
    nome = 'Elaine'
    idade = 48
    altura = 1.80
    peso = 70
    pais_origem = 'Brasil'
    genero = 'Feminino'

    #metodos - funções

    def dizer_ola():
        print(f'Olá, eu sou {ClassePessoa.nome}')
        
    def mostrar_dados():
        print(   
            f'Eu tenho {ClassePessoa.idade} anos, {ClassePessoa.altura} altura,' + 
            f'{ClassePessoa.peso}, peso e meu genero é {ClassePessoa.genero}'
        )
        
    def mostrar_origem():
        print(f'Eu venho de/do/da {ClassePessoa.pais_origem}')

ClassePessoa.dizer_ola()
ClassePessoa.mostrar_dados()
ClassePessoa.mostrar_origem()

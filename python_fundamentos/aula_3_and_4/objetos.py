class Pessoa:
    nome = 'Elaine'
    idade = 48
    origem = 'Brasil'

    def dizer_ola(self):
        print(f'Ola, eu sou {Pessoa.nome}')

    def pensar(self):
        print('Eu estou pensando.')

    def comprar(self):
        print('Compra realizada.')

    #getter para buscar nome
    def get_nome(self):
        return Pessoa.nome
    
    #getter para buscar idade
    def get_idade(self):
        return Pessoa.idade
    
    #setter para setar o nome
    def set_nome(self, nome_novo):
        Pessoa.nome = nome_novo

    def set_idade(self, idade_nova):
        Pessoa.idade = idade_nova

Pessoa_1 = Pessoa()
Pessoa_2 = Pessoa()

Pessoa_1.comprar()
Pessoa_2.comprar()
Pessoa_2.pensar()
Pessoa_1.pensar()

#chamado os getter
print(Pessoa_1.get_nome())
print(Pessoa_1.get_idade())

#chamado os setters
Pessoa_1.set_nome('Clarice')
print(Pessoa_1.get_nome())

#utilizando os setters
Pessoa_2.set_idade(18)
print(Pessoa_2.get_idade())


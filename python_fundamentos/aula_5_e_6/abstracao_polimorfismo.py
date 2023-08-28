from abc import ABC, abstractmethod

class PessoaAbstrata:

    @abstractmethod
    def gastar_dinheiro():
        pass

    @abstractmethod
    def respirar():
        pass

    @abstractmethod
    def falar():
        pass

class Atleta(PessoaAbstrata):
    #@staticmethod
    def gastar_dinheiro():
        print('Eu gasto pouco dinheiro!')

    def falar():
        print('Queremos um aumento!')

class Artista(PessoaAbstrata):
    #@staticmethod
    def gastar_dinheiro():
        print('Eu gasto muito dinheiro!')

    def falar():
        print('Eu sou rico e falo 5 idiomas!')

Artista.gastar_dinheiro()
Artista.falar()
Artista.respirar()
Atleta.gastar_dinheiro()
Atleta.falar()
Atleta.respirar()

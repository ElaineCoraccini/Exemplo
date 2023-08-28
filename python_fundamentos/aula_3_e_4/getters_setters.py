
class Animal():
    # raca = ''
    # cor = ''
    # idade = 0


    #private -> __nome
    #protested -> _nome
    #public = nome

    #construtor
    def __init__(self, raca, cor, idade, nome):
        self._raca = raca
        self._cor = cor
        self._idade = idade
        self.__nome = nome
        print('Objeto instanciado com sucesso.')

    @property #substitui o get
    def raca(self):
        return self._raca

    @property
    def cor(self):
        return self._cor
    @property
    def idade(self):
        return self._idade
    
    @property
    def nome(self):
        return self.__nome

    @raca.setter
    def raca(self, raca_nova):
        print(f'Setou raca {self._raca} para {raca_nova}')
        self._raca = raca_nova

    @cor.setter
    def cor(self, cor_nova):
        print(f'Setou cor {self._cor} para {cor_nova}')
        self._cor = cor_nova

    @idade.setter
    def idade(self, idade_nova):
        print(f'Setou idade {self._idade} para {idade_nova}')
        self._idade = idade_nova

    @idade.setter
    def nome(self, nome_nova):
        print(f'Setou idade {self.__nome} para {nome_nova}')
        self.__nome = nome_nova

if __name__ == '__main__':

    leao = Animal('leao da montanha', 'beje', 15, 'simba')
    gato = Animal('ciames', 'branco', 6, 'chato')
    pantera = Animal('pantera negra', 'preto', 3, 'king')

    print(leao.raca)
    print(leao.cor)
    print(leao.idade)
    print(leao.nome)

    print(gato.raca)
    print(gato.cor)
    print(gato.idade)
    print(gato.nome)

    print(pantera.raca)
    print(pantera.cor)
    print(pantera.idade)
    print(pantera.nome)

#usar setters
    pantera.idade = 20
    print(pantera.idade)
    pantera.cor = 'verde'
    gato.raca = 'Persa'
    print(pantera.nome)

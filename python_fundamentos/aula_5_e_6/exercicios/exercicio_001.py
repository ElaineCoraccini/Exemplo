# Crie uma classe abstrata chamada Animal com métodos falar(), comer() e mover().
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, idade, peso, cor):
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.cor = cor

    @abstractmethod
    def emitir_som(self):
        pass
    @abstractmethod
    def comer(self):
        pass
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def exibir_informacoes(self):
        pass

# Crie subclasses Cachorro, Cavalo e Gato que herdam da classe Animal e implementam

class Cavalo(Animal):
    def emitir_som(self):
        print('Prusxx... eeeeahhhaha')

    def comer(self):
        print('Comendo capim!')

    def mover(self):
        print('Pulando aleatoriamente!')

    def exibir_informacoes(self):
        print(f'\nEspécie {self.especie}')
        print(f'Idade {self.idade}')
        print(f'Peso {self.peso}')
        print(f'Cor {self.cor}')

class Cachorro(Animal):
    def emitir_som(self):
        print('au au au')

    def comer(self):
        print('Roendo osso!')

    def mover(self):
        print('Correndo atrás do carteiro!')

    def exibir_informacoes(self):
        print(f'\nEspécie {self.especie}')
        print(f'Idade {self.idade}')
        print(f'Peso {self.peso}')
        print(f'Cor {self.cor}')


class Gato(Animal):
    def emitir_som(self):
        print('miau miau')

    def comer(self):
        print('comento caixa de sapato!')

    def mover(self):
        print('Correndo atrás do rato!')

    def exibir_informacoes(self):
        print(f'\nEspécie {self.especie}')
        print(f'Idade {self.idade}')
        print(f'Peso {self.peso}')
        print(f'Cor {self.cor}')

# seus próprios métodos, printando frases diferentes.  
if __name__ == '__main__':
    cavalo_1 = Cavalo(
        especie= 'Marchador',
        idade= 10,
        peso= 155.5,
        cor= 'preto'
    )
    cavalo_2 = Cavalo(
        especie= 'Marchador',
        idade= 12,
        peso= 160.5,
        cor= 'mescla'
    )
    gato_objeto = Gato(
        especie= 'Siamês',
        idade= 6,
        peso= 5,
        cor= 'branco'
    )
    cachorro_objeto = Cachorro(
        especie= 'Labrador',
        idade= 12,
        peso= 16,
        cor= 'Caramelo'
    )

    cavalo_1.exibir_informacoes()
    cavalo_1.emitir_som()
    cavalo_1.mover()
    cavalo_1.comer()

    cavalo_2.exibir_informacoes()
    cavalo_2.emitir_som()
    cavalo_2.mover()
    cavalo_2.comer()

    gato_objeto.exibir_informacoes()
    gato_objeto.emitir_som()
    gato_objeto.mover()
    gato_objeto.comer()

    cachorro_objeto.exibir_informacoes()
    cachorro_objeto.emitir_som()
    cachorro_objeto.mover()
    cachorro_objeto.comer()


# Crie e trabalhe com os getters e setters para as subclasses.
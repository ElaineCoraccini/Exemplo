# Crie uma classe abstrata Animal  
# Crie uma função que aceita uma lista de animais e faça-os emitir sons usando polimorfismo.


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor

#crie um método emitir_som().
    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def informacao(self):
        pass

    
# Crie subclasses Cachorro,
# Gato, Cavalo e Vaca que herdam de Animal e implementam seus próprios sons.

class Cachorro(Animal):
    def emitir_som(self):
        return 'Cachorro: Au Au Au'
    
    def informacao(self):
        print(f'\nCachorro \nNome: {self.nome} \nCor: {self.cor}')


class Gato(Animal):
    def emitir_som(self):
        return 'Gato: Miau Miau Miau'
    
    def informacao(self):
        print(f'\nGato \nNome: {self.nome} \nCor: {self.cor}')


class Cavalo(Animal):
    def emitir_som(self):
        return 'Cavalo: Hiiiiiiii'
    
    def informacao(self):
        print(f'\nCavalo \nNome: {self.nome} \nCor: {self.cor}')


class Vaca(Animal):
    def emitir_som(self):
        return 'Vaca: Muuuuuuuuuu'
    
    def informacao(self):
        print(f'\nVaca \nNome: {self.nome} \nCor: {self.cor}')
    

def emitir_som(animais):
    for animal in animais:
        print(animal.emitir_som())

# Em seguida, crie contrutores para as subclasses dando um atributo nome e cor, e crie
# objetos dessas subclasses com cores e nomes distintos.

cachorro = Cachorro('Mike', 'Caramelo')
gato = Gato('Chato', 'Cinza')
cavalo = Cavalo('Spirit', 'Malhado')
vaca = Vaca('Mimosa', 'Branca')

cachorro.informacao()
print('\n')
gato.informacao()
print('\n')
cavalo.informacao()
print('\n')
vaca.informacao()
print('\n')

animais = [cachorro, gato, cavalo, vaca]
emitir_som(animais)
    
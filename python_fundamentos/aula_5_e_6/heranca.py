
#classe parente (mãe)
class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def correr(self):
        print(f'{self.nome} está correndo...')

    def comer(self):
        print(f'{self.nome} está se alimentando...')

#subclasse herdando classe animal
class Cachorro(Animal): 
    def latir(self):
        print(' au au - I am dog!')


class Gato(Animal):
    def miar(self):
        print('meau meau')

    def destruir_sofa(self):
        print('seu sofé foi destruido!')

cao_1 = Cachorro('bili', 'preto')
cao_1.correr()
cao_1.comer()
cao_1.latir()

gato_1 = Gato('mimi', 'branco')
gato_1.correr()
gato_1.comer()
gato_1.miar()
gato_1.destruir_sofa()


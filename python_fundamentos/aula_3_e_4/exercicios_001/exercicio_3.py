import time

# Crie uma classe chamada Carro que simule um carro. 
class Carro():

#A classe deve ter os atributos marca, modelo e ano.
        marca = 'Nissan'
        modelo = 'Kicks'
        ano = 2021
        ligado = False

# Crie métodos para ligar (ligar()), desligar (desligar())
        def ligar():
                        print('O carro ligou com sucesso!')
  
        def desligar():
                        print('Carro desligado com sucesso!')

        def descricao():
                print(
                        f'Este carro é do ano {Carro.ano}, marca {Carro.marca}, modelo {Carro.modelo}.'
                )

while True:
        metodo = input('Informe o nome dometodo: ')
        if metodo.lower() == 'ligar':
                Carro.ligar()
        elif metodo.lower() == 'desligar':
                Carro.desligar
        elif metodo.lower() == 'exibir':
                Carro.exibir_informacoes()
        elif metodo.lower() == 's':
                print('Programa encerrado.')
                break
        





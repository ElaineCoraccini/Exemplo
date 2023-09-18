import os


def mostrar_lista():
    lista_dados = [
        1,
        2,
        3,
        'hello',
        'hi',
        False,
        True,
        1.5,
        21,
        'texto!'
    ]

    for item in lista_dados:
        print(item)

def obter_mostrar_dados():
    lista_input = []

    for i in range(5):
        item = input(f'Informe o {i + 1}º item: ')
        lista_input.append(item)

    print('\nItens informados na lista: ')
    for item in lista_input:
        print(item)

def script_lista():
    lista_dados = []
    contador = 0
    # receber 10 itens do usuário
    while contador < 10 :
        contador += 1
        item_informado = input(f'Informe o {contador}º item: ')
        lista_dados.append(item_informado)

    
    # mostrar os itens recebidos
    # acessando tbm os indices, posição
    for indice, item in enumerate(lista_dados):
        print(f'Posição {indice} - Valor {item}')

    # loop para o usuário acessar itens especificos da lista
    while True:
        try:
            posicao_item = int(input('Informe a posição do item desejado: '))
            print(f'O item que esta na posição {posicao_item} é: {lista_dados[posicao_item]}')
            verificacao = input('Informe S para parar, ou outro valor para continuar: '.lower())
            if verificacao == 's':
                print('Programa Parou!!')
                break

        except:
            print('Informe apenas inteiros para posições em listas!')


# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    # mostrar_lista()
    # obter_mostrar_dados()
    script_lista()
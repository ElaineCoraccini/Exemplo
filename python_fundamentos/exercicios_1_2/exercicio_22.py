# Crie uma função para gerenciar os pedidos de um restaurante.
# O programa deve permitir que o usuário adicione novos pedidos, 
#remova pedidos prontos e exiba os pedidos pendentes.

import os

def gerenciar_pedidos():
    pedidos = []

    while True:
        print('1. Incluir o pedido')
        print('2. Excluir o pedido')
        print('3. Exibir pedidos pendetes')
        print('4. Sair')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            pedido = input('Digite o pedido: ')
            pedidos.append(pedido)
            print(f'Pedido {pedido} adicionado.')

        elif opcao == 2:
            if not pedidos:
                print('Não há pedidos para remover.')
            else:
                pedido = pedido.pop(0)    
                print(f'Pedido {pedido} removido')

        elif opcao == 3:
            if not pedidos:
                print('Não há pedidos pendentes.')
            else:
                print('Pedidos pendentes: ')
                for pedidos in pedidos:
                    print(pedido)

        elif opcao == 4:
            break
        else:
            print('Opção inválida.')

gerenciar_pedidos()
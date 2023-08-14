
# Crie uma classe chamada Agenda que represente uma agenda de contatos. A classe deve ter um atributo para armazenar uma lista de contatos.
import os

class Agenda:
    lista_contatos = []

# Crie métodos para adicionar (adicionar_contato(nome, telefone)), remover (remover_contato(nome)), e exibir todos os contatos (exibir_contatos()).
    @staticmethod
    def adicionar(item_lista):
        Agenda.lista_contatos.append(item_lista)
        print(f'Item {item_lista[0]} e telefone {item_lista[1]} adicinado com sucesso!')

    @staticmethod
    def remover(posicao):
        Agenda.lista_contatos.pop(posicao)
        print(f'Item na posição {posicao}, removido com sucesso!')

    @staticmethod
    def exibir_info():
        if len(Agenda.lista_contatos) > 0:
            for i in range(len(Agenda.lista_contatos)):
                print(f'\Posição -> {i} nome -> {Agenda.lista_contatos[i][0]} telefone -> {Agenda.lista_contatos[i][1]}')
            else:
                print('A lista está vazia!')

    @staticmethod
    def rodar_script():
        while True:
            try:
                metodo = input('Informe o método (s para sair): ')
                
                if metodo.lower() == 'adicionar':
                    novo_nome = input('Informe novo item: ')
                    novo_telefone = input('Informe o novo telefone: ')
                    Agenda.adicionar([novo_nome, novo_telefone])

                elif metodo.lower()  == 'remover':
                    posicao = int(input('Informe novo item: '))
                    Agenda.remover(posicao)

                elif metodo.lower()  == 'exibir':
                    Agenda.exibir_info()

                elif metodo.lower() == 's':
                    print('Programa encerrado.')
                    break

            except Exception as erro:
                print(f'Ocorreu um erro:')

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela de acordo com o sistema operacional veio chatgpt (digitar s não fechava)
    Agenda.rodar_script()

# 1 - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria que simule uma conta bancária simples.
# A classe deve ter os atributos titular, saldo e numero. Crie métodos para depositar (depositar(valor))
# e sacar (sacar(valor)) dinheiro da conta, além de um método para exibir o saldo atual (exibir_saldo()).

class ContaBancaria:
    mensagem_input = 'Informe 1 para depositar,'
    mensagem_input = 'Informe 2 para sacar, 3 para exibir e 4 para sair: '
    titular = ''
    numero = 0
    saldo = 0

    def depositar(valor):
       
        try:
           valor = float(valor)
           ContaBancaria.saldo += valor
        except:
           print('Informe um valor válido para depósito!')       

    def sacar(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo -= valor
        except:
            print('Informe um valor válido para sacar!')
     
    def exibir():
        print(
            f'Titular {ContaBancaria.titular} com número {ContaBancaria.numero} tem saldo {ContaBancaria.saldo}'
        )
    
    def script():
        while True:
            try:
                opcao = input(ContaBancaria.mensagem_input)
                if opcao == '1':
                    valor = input('Informe o valor: ')
                    ContaBancaria.deposita(valor)
                elif opcao == '2':
                    valor = input('Informe o valor: ')
                    ContaBancaria.sacar(valor)                
                elif opcao == '3':
                    valor = input('Informe o valor: ')
                    ContaBancaria.exibe()                
                elif opcao == '4':
                    print('Volte sempre com dinheiro!!')
                    break
            except:
                print('Informe uma opção válida!')

if __name__ == '__main__':
    ContaBancaria.script()
                    




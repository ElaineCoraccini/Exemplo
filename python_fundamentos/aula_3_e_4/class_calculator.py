
class Calculator:
    operacoes_limite = 10
    input_mensagem = 'Informe um numero entre 1 e 5: '
    input_mensagem += '\n1 = somar'
    input_mensagem += '\n2 = subtrair'
    input_mensagem += '\n3 = multiplicar'
    input_mensagem += '\n4 = dividir'
    input_mensagem += '\n5 = modulo'
    input_mensagem += '\ninforme a opçao: '

    def somar(numero_1, numero_2):
        print(f'\33[032m A soma dos numeros é {numero_1 + numero_2} \33[0m')

    def subtrair(numero_1, numero_2):
        print(f'\33Subtrair-Resultado: {numero_1 - numero_2} \33[0m')


    def multiplicar(numero_1, numero_2):
        print(f'\33Multiplica-Resultado: {numero_1 * numero_2} \33[0m')
    

    
    def dividir(numero_1, numero_2):
        print(f'\33Dividir-Resultado: {numero_1 / numero_2} \33[0m')

    def modulo(numero_1, numero_2):
        print(f'\33Resto- Div-Resultado: {numero_1 % numero_2} \33[0m')

    def controle_operacoes():
        contador = 0
        while contador < Calculator.operacoes_limite:
            contador += 1

            try:
                print(f'\nOperação {contador}')
                numero_1 = int(input('Informe o primeiro numero: '))
                numero_2 = int(input('Informe o segundo numero: '))

                if numero_1 > 0 and numero_2 > 0:
                    while True:
                        try:
                            opcao = int(input(Calculator.input_mensagem))
                            if opcao == 1:
                                Calculator.somar(numero_1, numero_2)
                                break
                            elif opcao == 2:
                                Calculator.subtrair(numero_1, numero_2)
                                break
                            elif opcao == 3:
                                Calculator.multiplicar(numero_1, numero_2)
                                break
                            elif opcao == 4:
                                Calculator.dividir(numero_1, numero_2)
                                break
                            elif opcao == 5:
                                Calculator.modulo(numero_1, numero_2)
                                break     
                            else:
                                raise ValueError()              
                        except:
                            print('Informe uma opção válida!')
                else:
                    print('Informe números positivos!')
            except KeyboardInterrupt:
                print('n\Programa encerrado manualmente')
                quit()
            except:
                print('Informe um numero válido!')

if __name__ == '__main__':
    Calculator.controle_operacoes()

import os
from review_db import LogicaBanco


#e negativosemoutras funções
#a função deve retornar um boolean dependend do numero
class LogicaProgramacao(LogicaBanco):

    def eh_positivo(self, numero_parametro):
        if numero_parametro > 0:
            return True
        else:
            return False
        
    #funcao para veirifcar se um numero e positivo ou negativo
    # obs: usar essa funçãopara verificar numeros positivos
    def sao_numeros_iguais(self, numero_parametro_1, numero_parametro_2):
        if self.eh_positivo(numero_parametro_1) and self.eh_positivo(numero_parametro_2):
            if numero_parametro_1 == numero_parametro_2:
                return True
            else:
                return False
        else:
            print('Informar apenas numeros positivos!')

    #funcao verificar e retornar numero de dois numeros eh o maior
    #se ambos forem numeros positivos
    def retorna_maior_numero(self, numero_parametro_1, numero_parametro_2):
        numero_maior = None

        if self.eh_positivo(numero_parametro_1) and self.eh_positivo(numero_parametro_2):
            if numero_parametro_1 > numero_parametro_2:
                numero_maior = numero_parametro_1

            elif numero_parametro_1 < numero_parametro_2:
                numero_maior = numero_parametro_2 

            else:
                print('Os numero informados são iguais, informa numeros diferentes!')

        else:
            print('Informar apenas numeros positivos!')

        return numero_maior
        


    #funcao para verificar qual o numero de dois eh menor
    #se ambos forem numeros positivos
    def retorna_menor_numero(self, numero_parametro_1, numero_parametro_2):
        numero_menor = None

        if self.eh_positivo(numero_parametro_1) and self.eh_positivo(numero_parametro_2):
            if numero_parametro_1 < numero_parametro_2:
                numero_menor = numero_parametro_1

            elif numero_parametro_1 > numero_parametro_2:
                numero_menor = numero_parametro_2 

            else:
                print('Os numeros informados são iguais, informa numeros diferentes!')

        else:
            print('Informar apenas numeros positivos!')

        return numero_menor


    def retorna_par_ou_impar(self, numero_parametro):
        resultado = ''

        if self.eh_positivo(numero_parametro):
            if numero_parametro % 2 ==0:
                resultado = 'par'
            else:
                resultado = 'impar'
        else:
            print('Informar apenas numeros positivos!')

        return resultado

    #funcao para verificar qual o numero de uma lista de numeros é maior
    #usar for para achar maior numero
    def retorna_maior_numero_da_lista(elsf, lista_de_dados):
        maior_numero = None

        maior_numero = lista_de_dados[0]

        for item in lista_de_dados:
            if item > maior_numero:
                maior_numero = item

        return maior_numero


    def retorna_menor_numero_da_lista(self, lista_de_dados):
        menor_numero = None

        menor_numero = lista_de_dados[0]

        for item in lista_de_dados:
            if item < menor_numero:
                menor_numero = item

        return menor_numero

    def retorna_quant_de_impar_e_par_lista(self, lista_parametro):
    
        contador_par = 0
        contador_impar = 0

        for registro in lista_parametro:
            if registro % 2 == 0:
                contador_par += 1
            else:
                contador_impar += 1

        return contador_par, contador_impar


    #funcao para somar, dividir, subtrair e multiplicar dois numero,
    #dependendo da operação enviada por parametro
    def rodar_calculadora(self, numero_1, numero_2, operacao):
        resultado = None

        if operacao == 1:
            return numero_1 + numero_2
        if operacao == 2:
            return numero_1 - numero_2
        if operacao == 3:
            return numero_1 * numero_2
        if operacao == 4:
            return numero_1 / numero_2
        return resultado

    #VER GIT APARTIR DAQUI

    # funcao para verificar quantas vezes uma letra especificada pelo usuario aparece 
    # dentro de um texto tambem informado pelo usuario e mostre quantas vezes 
    # numeros de 1 a 9 aparecem caso tenha numeros no texto
    def contar_letras_e_numeros(self, letra, texto):
        if len(letra) == 1:
            contar_letra = 0
    # contar_numero = [0] * 10  # Inicializa um contador para cada número de 0 a 9
            contar_numero = 0
            lista_texto = list(texto)


        letra = letra.lower()

        for digito in texto:
            if digito == letra: 
                contar_letra += 1

            elif digito.isdigit():
                numero = int(digito)
                if 1 <= numero <= 9:
                    contar_numero[numero] += 1

        return contar_letra, contar_numero
        

    # funcao para verificar quanto um funcionario ganhou *durante um mes*,
    # com base no valor que o colaborador *ganha por hora* e em *quantos dias*
    # aquele mes atual tem. Passar tbm a *quantidade de horas trabalhadas por dia*
    # Todas essas informacoes devem ser passadas por parametro
    def calcular_salario(self, dias_trabalhados, horas_diarias, valor_hora):
        resultado = dias_trabalhados * horas_diarias * valor_hora
        return resultado  


    # funcao para verificar quantos items existem em uma lista no total,
    # mas também a quantidade de itens que sao string ou ints ou floats dentro da lista.
    # A função deve retornar a quantidade de cada um. Quando os dados forem enviados pelo
    # usuario via input, a lista precisa ter pelo menos 6 itens, dois sendo inteiros,
    # dois sendo floats e dois sendo strings antes de chamar a funcao
    def organizador_lista(self, lista_de_dados):
        contador_str = 0
        contador_int = 0
        contador_float = 0

        for item in lista_de_dados:
            if type(item) == str:
                contador_str += 1
            elif type(item) == int:
                contador_int += 1
            elif type(item) == float:
                contador_float += 1

        return contador_str, contador_int, contador_float

    def valida_lista_dinamica(self, lista):
        contador_str = 0
        contador_int = 0
        contador_float = 0

        for item in lista:
            if type(item) == str:
                contador_str += 1
            elif type(item) == int:
                contador_int += 1
            elif type(item) == float:
                contador_float +=1
        
        if contador_str >= 2 and contador_int >= 2 and contador_float >= 2:
            return True

        return False


    def receber_lista_usuario(self):
        lista_retorno = []

        while True:
            try:
                item = input(
                    f'Informe o {len(lista_retorno) + 1}º item (p para parar): '
                )

                if item != 'p':
                    try:
                        item = int(item)
                        lista_retorno.append(item)
                        continue                
                    except:
                        try:
                            item = float(item)
                            lista_retorno.append(item)
                            continue                
                        except:
                            pass
                
                    lista_retorno.append(item)
                else:
                    if len(lista_retorno) >= 6:
                        print(f'Foram inseridos {len(lista_retorno)} itens!')
                        break
                    else:
                        print('A lista precisa de pelo menos 6 itens!')
            except Exception as e:
                print(f'Erro: {str(e)}')
        
        return lista_retorno



    def main(self):
        menu_main= f'''
\nSelecione a função:
0 - Sair
1 - eh_positivo
2 - sao_numeros_iguais
3 - retorna_maior_numero
4 - retorna_menor_numero
5 - verifica_se_eh_impar_ou_par
6 - retorna_maior_numero_em_lista
7 - retorna_menor_numero_em_lista
8 - retorna_quantidade_de_impares_e_pares_em_lista
9 - rodar_calculadora
10 - verifica_letra_em_string
11 - calcular_salario
12 - organizador_lista
--> opcao      
   '''
        
        #self.criar.conexao(LogicaBanco)

        while True:

            registro.string = ''
            funcao_selecionada = int(input{menu})


            ##Inserir mensagens na variável registro string
            ##dentro de ltodos os elifs com operações

            try:
                funcao_selecionada = int(input(menu_main))
                if funcao_selecionada == 0:
                    print('O programa encerrou!')
                    break

                elif funcao_selecionada == 1:
                    numero = int(input('Informe um numero: '))

                    if self.eh_positivo(numero) is True:
                        print(f'O numero {numero} é positivo')
                    else:
                        print(f'O numero {numero} é negativo')

                elif funcao_selecionada == 2:
                    numero_1 = int(input('Informe o primeiro numero: '))
                    numero_2 = int(input('Informe o segundo numero: '))

                    if self.sao_numeros_iguais(numero_1, numero_2) is True:
                        print(f'O numero {numero_1} é igual ao numero {numero_2}')
                    else:
                        print(f'O numero {numero_1} é diferente do numero {numero_2}')

                elif funcao_selecionada == 3:
                    numero_1 = int(input('Informe o primeiro numero: '))
                    numero_2 = int(input('Informe o segundo numero: '))

                    numero_retornado = self.retorna_maior_numero(numero_1, numero_2)
                    if  numero_retornado != None:
                        print(f'O maior numero é: {numero_retornado}')   

                elif funcao_selecionada == 4:
                    numero_1 = int(input('Informe o primeiro numero: '))
                    numero_2 = int(input('Informe o segundo numero: '))

                    numero_retornado = self.retorna_menor_numero(numero_1, numero_2)
                    if  numero_retornado != None:
                        print(f'O menor numero é: {numero_retornado}')              

                elif funcao_selecionada == 5:
                    numero = int(input('Informe um numero: ')) 
                    resultado = self.retorna_par_ou_impar(numero)

                    if resultado != '':
                        print(f'O numero {numero} é {resultado}!')

                elif funcao_selecionada == 6:
                    lista_de_dados = []
                    contador = 0
                    limite = int(input('Informe a quantidade de itens desejado na lista: '))

                    while contador < limite:
                        try:
                            item = int(input(f'Informe o {contador + 1}º item:'))
                            lista_de_dados.append(item)
                            contador += 1
                        except:
                            print ('Informum numero válido.')
                
                    maior_numero = self.retorna_maior_numero_da_lista(lista_de_dados)
                    if maior_numero != None:
                        print(f'O maior numero da lista é: {maior_numero}')

                elif funcao_selecionada == 7:
                    lista_de_dados = []
                    contador = 0
                    limite = int(input('Informe a quantidade de itens desejado na lista: '))

                    while contador < limite:
                        try:
                            item = int(input(f'Informe o {contador + 1}º item:'))
                            lista_de_dados.append(item)
                            contador += 1
                        except:
                            print ('Informum numero válido.')
                
                    menor_numero = self.retorna_menor_numero_da_lista(lista_de_dados)
                    if menor_numero != None:
                        print(f'O maior numero da lista é: {menor_numero}')


                elif funcao_selecionada == 8:
                    lista_de_dados = []
                    contador = 0
                    limite = int(input('Informe a quantidade de itens desejado na lista: '))

                    while contador < limite:
                        try:
                            item = int(input(f'Informe o {contador + 1}º item:'))
                            lista_de_dados.append(item)
                            contador += 1
                        except:
                            print ('Informum numero válido.')
                
                    contador_par, contador_impar = self.retorna_quant_de_impar_e_par_lista(lista_de_dados)
                    print(f'A quantidade de pares é {contador_par} e de impares é {contador_impar}')
                
                elif funcao_selecionada == 9:
                    numero_1 = int(input(f'Informe o primeiro numero: '))
                    numero_2 = int(input(f'Informe o segundo numero: '))

                    menu_operacoes = '''
                    \nOperações:
                    1- Somar
                    2- Subtrair
                    3- Multiplicar
                    4- Dividir
                    --> opção: '''

                    while True:
                        try:
                            operacao = int(input(menu_operacoes))
                            if operacao in [1, 2, 3, 4]:
                                resultado = self.rodar_calculadora(numero_1, numero_2, operacao)
                                print(f'O resultado da operação é: (resultado)')
                                break
                            else:
                                print('Informe uma operação válida!')
                        except:
                            print('Informe um número válido.')

                elif funcao_selecionada == 10:
                    letra = input('Informe a letra: ')
                    texto = input('Informe o texto: ')
                    
                    if len(letra) == 1 and len(texto) >= 10:
                        letras, numeros = self.contar_letras_e_numeros(letra, texto)
                        print(f'A letra {letra} apareceu {letras}')
                        print(f'Apareceram {numeros} numeros')
                        print(f'dentro do texto: {texto}')
                    else:
                        print('Informe apenas uma letra', end=' ')
                        print('e um texto com pelo menos 10 letras.')

                elif funcao_selecionada == 11:
                    try:
                        dias = int(input('Informe a quantidade de dias: '))
                        horas = int(input('Informe a quantidade de horas: '))
                        valor = int(input('Informe o valor da hora: '))

                        if dias >= 15 and horas >= 6 and valor >= 10:
                            resultado = self.calcular_salario(
                                dias_trabalhados=dias,
                                horas_diarias=horas,
                                valor_hora=valor
                            )

                            print(f'O resultado é: {resultado}')
                        else:
                            print(
                                'Informe valores válidos!'
                            )
                    except Exception as e:
                        print(f'Erro: {str(e)}')
                        print('Informe números válidos!')
                    
                elif funcao_selecionada == 12:
                    lista = self.receber_lista_usuario()
                    if self.valida_lista_dinamica(lista) == True:
                        strings, ints, floats = self.organizador_lista(lista)
                        print(f'Na lista informada existem {strings} strings', end=' ')
                        print(f'{ints} inteiros, e {floats} floats')
                    else:
                        print('A lista precisa de pelos menos', end=' ')
                        print('2 strings, 2 ints e 2 floats!')

            except Exception as e:
                print(f'Erro: {e}')    

        


if __name__ == '__main__':
    os.system('cls') #limpar terminal
    #main()
    objeto_da_classe = LogicaProgramacao()
    print('rodando...')
    objeto_da_classe.main()

 



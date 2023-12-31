# Exercício 8:
# Crie uma função que solicite ao usuário que insira a data de nascimento no formato "dd/mm/aaaa" e armazene o dia,
# mês e ano em variáveis diferentes. Mostre uma mensagem com as variáveis separadas.
import os

from datetime import datetime

def recebe_data():
    while True:
        try:
            dia = int(input('Informe o dia: '))
            if dia > 0 and dia <= 31:
                mes = int(input('Informe o mes: '))
                if mes > 0 and mes <= 12:
                    ano = int(input('Informe o ano: '))
                    if ano >= 1950 and ano <= 2023:
                        return dia, mes, ano
                    else:
                        print('Ano inválido')
                else:
                    print('mês inválido')
            else:
                print('dia inválido!')
        except:
            print('Informe datas válidas!')

def mostrar_data(dia, mes, ano):
    print(f'A data informada foi {dia}/{mes}/{ano}')

def main():
    dia, mes, ano = recebe_data()
    mostrar_data(dia, mes, ano)
   
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    main()
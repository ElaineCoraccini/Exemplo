#Crie uma função que converta um valor em dólar para real. 
#Peça ao usuário que insira a cotação do dólar e o valor em dólar a ser convertido. 
#Em seguida, exiba o valor equivalente em reais.

import os

def converter_dolar_real():
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
    valor_dolar = float(input("Digite o valor em dólar a ser convertido: "))
    conversao = valor_dolar * cotacao_dolar
    
    print(f"O valor convertido em reais é: R${conversao}")

def main():
    converter_dolar_real()

if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    main()
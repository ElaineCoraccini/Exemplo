#Crie uma função que converta um valor em dólar para real. 
#Peça ao usuário que insira a cotação do dólar e o valor em dólar a ser convertido. 
#Em seguida, exiba o valor equivalente em reais.

def converter_dolar_real():
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
    valor_dolar = float(input("Digite o valor em dólar a ser convertido: "))
    valor_real = valor_dolar * cotacao_dolar
    
    print(f"O valor equivalente em reais é: R$ {round(valor_real, 2)}")

# def main():
#     cotacao_dolar, valor_dolar, valor_real = converter_dolar_real()
#     mostrar_data(dia, mes, ano)

# if __name__ == '__main__':
#     os.system ('cls')
#     os.system ('python --version')
#     main()
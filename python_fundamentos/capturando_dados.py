import os

def captura_dados():
    # Lendo dados do usuário
    texto_usuario = input('Informe um texto: ')
    print('Você escreveu: ', texto_usuario)
    print (type(texto_usuario))

    inteiro_usuario = input('Informe um número: ')
    # Try para tentar executar o código e continuar caso haja erro:
    try:
        inteiro_usuario = int(inteiro_usuario)
    except:
        print('Erro ao tentar converter inteiro!')
    print('Você informou o número: ', inteiro_usuario)
    print (type(inteiro_usuario))

    float_usuario = input('Informe um número float: ')
    # Try para tentar executar o código e continuar caso haja erro:
    try:
        float_usuario = float(float_usuario)
    except:
        print('Erro ao tentar converter float!')
    print('Você digitou o número: ', float_usuario)
    print (type(float_usuario))

# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__== '__main__':
    os.system ('cls')
    print('Executando 1ª vez!')
    captura_dados()
    print('Executando 2ª vez!')
    captura_dados()
    print('Executando 3ª vez!')
    captura_dados()
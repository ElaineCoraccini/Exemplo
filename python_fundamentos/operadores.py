import os

def verifica_numeros():
    try:
        primeiro_num = int(input('Informe um número: '))
        segundo_num = int(input('Informe outro Número: '))

        if primeiro_num > 0 and segundo_num > 0:
            if primeiro_num != segundo_num:
                if primeiro_num > segundo_num:
                    print('Primeiro número é maior que o segundo número!!')
                elif primeiro_num < segundo_num:
                    print('Primeiro número é menor que o segundo número!!')
            elif primeiro_num == segundo_num:
                print('Números informados são iguais!!')
        else:
            print('Números precisam ser positivos!!')
    except:
        print('Erro ao converter os dados para Int!!')

def verifica_idade():
    try:
        idade_usuario = int(input('Informe sua idade: '))

        if idade_usuario > 0 and idade_usuario < 121:
            # Verificar se é adulto ou nao
            if idade_usuario >= 18:
                print('Você é um adulto!')
            elif idade_usuario >= 10 and idade_usuario < 18:
                print('Você é um Teen')
            elif idade_usuario < 12:
                print('Você é uma criança')
        else:
            print('Idade Inválida! Impostor!!!!')
    except:
        print('Erro ao ler dados!!')


# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    verifica_numeros()
    verifica_idade()
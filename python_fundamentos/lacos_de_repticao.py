import os
# importar função de outro arquivo
from operadores import verifica_idade
from operadores import verifica_numeros


def script_idade():
    while True:
        # rodar funcao da idade
        verifica_idade()

        # verificar se deve continuar
        verificacao = input('Informe S para Sair, e qualquer outro char para continuar: ')

        # deixar letras minusculas
        verificacao = verificacao.lower()

        # parar loop
        if verificacao == 's':
            break

def script_numeros(limite_loop):
    contador = 0
    while contador < limite_loop:
        # os.system ('cls')
        contador += 1
        verifica_numeros()

    print(f'O loop rodou {limite_loop} vezes!')

    

# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    # script_idade()
    limite_loop = int(input('Informe quantas vezes o programa deve rodar: '))
    script_numeros(limite_loop)
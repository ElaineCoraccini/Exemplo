# exercicio 4
# Desenvolva uma função que mostre na tela uma contagem regressiva de 5 a 1, com uma pausa de um segundo 
# entre cada número.

import os
import time

def contagem_regressiva():
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    
    print("Contagem regressiva concluída!")

def contagem_regressiva_manual():
    contador = 5
    while contador > 0:
        print(contador)
        time.sleep(1)
        contador -= 1

# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    # contagem_regressiva()
    contagem_regressiva_manual()
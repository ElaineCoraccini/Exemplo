import os
# Crie uma classe chamada Aluno que represente um aluno. 

class Aluno():

#A classe deve ter os atributos nome, matricula e notas (uma lista de notas).
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

# Crie métodos para calcular a média (calcular_media()) 
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
#exibir o status do aluno com base na média (exibir_status()).    
    def exibir_status(self):
        media = self.calcular_media()
        if media >= 7:
            return 'Aprovado'
        else:
            return 'Reprovado'      

if __name__ == '__main__':
    nome_aluno = input("Digite o nome do aluno: ")
    matricula_aluno = input("Digite a matrícula do aluno: ")
    notas_aluno = [float(nota) for nota in input("Digite as notas do aluno separadas por espaço: ").split()] #esta função veio chatgpt
    
    aluno = Aluno(nome_aluno, matricula_aluno, notas_aluno)
    
    # Exibir o status do aluno
print("Status do aluno:", aluno.exibir_status())


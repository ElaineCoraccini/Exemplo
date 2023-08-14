

#Crie uma classe chamada Livro que represente um livro.
class Livro:

#A classe deve ter os atributos titulo, autor e ano.
    titulo = 'Mulheres que correm com lobos'
    autor = 'Clarissa P Estes'
    ano = 1992

#Crie um método para exibir as informações do livro (exibir_informacoes()).
    def exibir_informacoes():

        print(f'\nLivro: {Livro.titulo} / Autor: {Livro.autor} / Ano: {Livro.ano}')

Livro.exibir_informacoes()        


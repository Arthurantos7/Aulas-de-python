import os
import sys
import time
from dataclasses import dataclass 
os.system("clear")
livro = []
# Contante.

def cabecalho():
 os.system("cls||clear")
 print(f"===SENAI===")
QUANTIDADE_ALUNOS = 2

class Livros:
    def __init__(self, n1:str,n2:str,n3,n4):
        self.titulo = n1
        self.autor = n2
        self.pagNumero = n3
        self.preco = n4

for i in range(QUANTIDADE_ALUNOS):
    cabecalho()
    tituloLivro = input(f"Digite o nome do {i + 1}º livro:")
    nomeAutor = input(f"Digite o nome do autor do {i + 1}º livro:")
    numeroPagina = input(f"Digite o número de paginas do {i + 1}º livro:")
    precoLivro = input(f"Digite o preço do {i + 1}º livro:")
    livro.append(Livros(tituloLivro,nomeAutor,numeroPagina,precoLivro))

for i,j in enumerate(livro):
    print(f"===== {i +1}º livro ====")
    print(f"Titulo: {j.titulo}")
    print(f"Autor: {j.autor}")
    print(f"Número de paginas: {j.pagNumero}")
    print(f"Preço do livro: {j.preco}")
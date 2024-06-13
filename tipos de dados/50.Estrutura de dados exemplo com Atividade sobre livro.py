import os
import sys
import time
from dataclasses import dataclass 

os.system("clear")

# Contante.
QUANTIDADE_LIVROS = 2

#classes
@dataclass
class Livro:
    titulo: str
    autor: str
    numeroPaginas: int
    preco: float

livros = []

# Solicitando dados para o usuário.
for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        titulo = input("Digite o titulo: "),
        autor = input("Digite seu autor: "),
        numeroPaginas = int(input("Digite a quantidade de páginas: ")),  
        preco = float(input("Digite o preço: "))   
    )
    livros.append(livro)

# Exibindo dados para o usuário.
for i in livros:
    os.system("clear")
    print(f"======= DADOS ======")
    print(f"Titulo: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Número de Páginas: {i.numeroPaginas}")
    print(f"Preço: {i.preco}")
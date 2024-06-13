import os
import sys
import time
from dataclasses import dataclass 
os.system("clear")
# Contante.
QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade: int

alunos = []

# Solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNOS):
    nome_do_aluno = input("Digite seu nome: ")
    idade_do_aluno = int(input("Digite sua idade: "))

    aluno = Aluno(nome = nome_do_aluno, idade = idade_do_aluno)
    alunos.append(aluno)

# Exibindo dados para o usuário.
for i in alunos:
    
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
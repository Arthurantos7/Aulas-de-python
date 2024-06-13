import os
import sys
import time
from dataclasses import dataclass 

os.system("clear")

# Contante.
QUANTIDADE_ALUNOS = 2

#classes
@dataclass
class Aluno:
    nome: str
    idade: int
    peso: int
    altura: float
alunos = []

# Solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        peso = int(input("Digite seu peso: ")),  
        altura = float(input("Digite sua altura: "))   
    )
    alunos.append(aluno)

# Exibindo dados para o usuário.
os.system("clear")
for i in alunos:
    print(f"======= DADOS ======")
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Peso: {i.peso}")
    print(f"Altura: {i.altura}")
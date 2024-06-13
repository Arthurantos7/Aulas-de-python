import os
import sys
import time
from dataclasses import dataclass 

os.system("clear")
pets = []
# Contante.

def cabecalho():
 os.system("clear")
 print(f"===PETSHOP===")
QUANTIDADE_PETS = 2

class Pet:
    def __init__(self, n1:str,n2,n3:str,n4:str,n5:str):
        self.nome = n1
        self.idade = n2
        self.raca = n3
        self.porte = n4
        self.alimentacao = n5

for i in range(QUANTIDADE_PETS):
    cabecalho()
    nome = input(f"Digite o nome do {i + 1}º pet: ")
    idade = int(input(f"Digite a idade do {i + 1}º pet: "))
    raca = input(f"Digite a raça do {i + 1}º pet: ")
    porte = input(f"Digite o porte do {i + 1}º pet: ")
    alimentacao = input(f"Digite a alimentação do {i + 1}º pet: ")
    Pet.append(pets(nome,idade,raca,porte,alimentacao))

for i,j in enumerate(Pet):
    print(f"===== {i +1}º DADOS DO PET ====")
    print(f"Nome: {j.nome}")
    print(f"Idade: {j.idade}")
    print(f"Raça: {j.raca}")
    print(f"Porte: {j.porte}")
    print(f"Alimentação do pet: {j.alimentacao}")
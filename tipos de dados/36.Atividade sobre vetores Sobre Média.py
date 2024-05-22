import os
import sys
import time

os.system("clear")

# Criando  uma lista / vetor
notas = []
soma = 0
media = 0

# Solicitando 3 notas para o usuário
for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    soma += notas[i]

media = soma  / 3


#Exibindo as notas para o usuário
os.system("clear")
print(f"Resultado de Média: {media: .1f}")    
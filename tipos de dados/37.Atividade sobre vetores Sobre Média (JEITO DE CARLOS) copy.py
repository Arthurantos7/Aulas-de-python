import os
import sys
import time

os.system("clear")
# Criando uma constante
QUNATIDADE_NOTAS = 3

# Criando  uma lista / vetor
notas = []

# Solicitando 3 notas para o usuário
for i in range(QUNATIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas)  / QUNATIDADE_NOTAS


#Exibindo as notas para o usuário
for i in range(QUNATIDADE_NOTAS):
    print(f"Nota: {notas[i]}")    

# ForEach
for i in notas:
    print(f"Nota: {nota}")

# Exibindo Média
print(f"Resultado de Média: {media: .1f}")    

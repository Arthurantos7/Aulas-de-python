import os
import sys
import time

os.system("clear")
QUANTIDADE_NUMEROS = 5

numeros = []

pares = 0
impares = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º Número: "))
    numeros.append(numero)

    if numero % 2 == 0:
       pares += 1   
    else:
      impares +=1 


for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")


print(f"Quantidade de Números pares: {pares}")
print(f"Quantidade de Números impares: {impares}")


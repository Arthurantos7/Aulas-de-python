import os
import sys
import time

os.system("clear")
QUANTIDADE_NUMEROS = 5

numeros = []
numero = 0
while True:
    numero = float(input("Digite um número:" ))
    if numero == 0:
        break
    numeros.append(numero)    

maiorNumero = max(numeros)
menorNumero = min(numeros)


for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")

print(f"Maior Número: {maiorNumero}")    
print(f"Menor Número: {menorNumero}")    

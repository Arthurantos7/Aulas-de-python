import os
import time

os.system("clear")
somaGeral = 0
quantidadeGeral = 0
somaPares = 0
pares = 0
impares = 0

while True:
    numero = int(input("Digite um número: "))    
    
    if numero > 0:
        somaGeral += numero
        quantidadeGeral += 1
        
        if numero % 2 == 0:
            somaPares += numero
            pares += 1
      
        else:
            impares += 1
    
    if numero == 0:
       break
  

mediaGeral = somaGeral / quantidadeGeral

if pares != 0:
    mediaPares = somaPares / pares


else:
    mediaPares = 0

print(f"Quantidade de números Pares: {pares}")
print(f"Quantidade de números Ìpares: {impares}")
print(f"Média Pares: {mediaPares}")
print(f"Média Geral: {mediaGeral}")
    
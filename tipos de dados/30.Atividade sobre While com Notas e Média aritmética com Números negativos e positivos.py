import os
import time

os.system("clear")
soma = 0
contador = 0
numero = 0
while True:
    numero = float(input(f"Insira um número: "))
    
    if (numero >= 0):
        soma += numero
        contador += 1 
    else:
        break   

media = soma / contador

print(f"=== EXIBINDO RESULTADOS ===")
print(f"média: {media}")
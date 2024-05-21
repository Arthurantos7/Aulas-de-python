import os
import sys

os.system("clear")

media = 0
soma = 0

("==== SOLICIANDO DADOS ====")
primeiroNumero = float (input("Digite o primeiro Número: "))
segundoNumero = float (input("Digite o primeiroo Número: "))

soma = primeiroNumero + segundoNumero 
media = (primeiroNumero + segundoNumero) / 2

os.system("clear")
print(f"=== EXIBINDO RESULTADOS  =====")
print(f"Primeiro Número: {primeiroNumero}")
print(f"Segundo Número: {segundoNumero}")
print(f"Resultado da Média: {media}")
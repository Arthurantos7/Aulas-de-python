#Tipagem dinâmica
import os

os.system("cls || clear")

print("=== Solicitando dados === \n")
PrimeiroNumero = int (input("Digite o Primeiro Número: ")) 
SegundoNumero = int (input("Digite o Segundo Número: ") )

subtracao = PrimeiroNumero - SegundoNumero
multiplicacao = PrimeiroNumero * SegundoNumero
divisao = PrimeiroNumero / SegundoNumero
soma = PrimeiroNumero + SegundoNumero

print(f"Primeiro Número: {PrimeiroNumero}")
print(f"Segundo Número: {SegundoNumero}")
print(f"resultado da subtracao: {subtracao}")
print(f"resultado da multiplicacao: {multiplicacao}")
print(f"resultado da divisao: {divisao}")
print(f"resultado da soma: {soma}")

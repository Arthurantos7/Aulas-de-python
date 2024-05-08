#Tipagem dinâmica
import os

os.system("cls || clear")

media: float = 0
soma: float = 0
multiplicacao = 0

print("=== Solicitando dados === \n")
primeiroNumero = float (input("Digite o Primeiro Número: ") )
segundoNumero = float (input("Digite o Segundo Número: ") )
terceiroNumero = float (input("Digite o Terceiro Número: ") )
quartoNumero = float (input("Digite o Quarto Número: ") )

soma = primeiroNumero + segundoNumero + terceiroNumero + quartoNumero
media = (primeiroNumero + segundoNumero + terceiroNumero + quartoNumero) / 4
multiplicacao = primeiroNumero * segundoNumero * terceiroNumero * quartoNumero

print(f"==== Exibindo Resultados:")
print(f"Primeiro Número: {primeiroNumero}")
print(f"Segundo Número: {segundoNumero}")
print(f"Terceiro Número: {terceiroNumero}")
print(f"Quarto Número: {quartoNumero}")
print(f"Resultado da Soma: {soma}")
print(f"Resultado da multiplicação: {multiplicacao}")
print(f"Resultado da média: {media}")


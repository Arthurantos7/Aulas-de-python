#Tipagem dinâmica
import os

os.system("cls || clear")

media: float = 0
soma: float = 0
multiplicacao = 0

print("=== Solicitando dados === \n")
primeiroNumero = float (input("Digite o Primeiro Número: ") )
segundoNumero = float (input("Digite o Segundo Número: ") )

soma = primeiroNumero + segundoNumero
media = (primeiroNumero + segundoNumero) / 2
multiplicacao = primeiroNumero * segundoNumero

print(f"==== Exibindo Resultados:")
print(f"Primeiro Número: {primeiroNumero}")
print(f"Segundo Número: {segundoNumero}")
print(f"Resultado da Soma: {soma}")
print(f"Resultado da multiplicação: {multiplicacao}")
print(f"Resultado da média: {media}")

if primeiroNumero < segundoNumero:
    maiorNumero = segundoNumero
    menorNumero = primeiroNumero
else:
    Maiornumero = primeiroNumero
    menorNumero = segundoNumero
print(f"Maior valor: {maiorNumero}")    
print(f"Menor valor: {menorNumero}")    
print(f"FIM DO RESULTADO")
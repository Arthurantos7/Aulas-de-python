#Tipagem dinâmica
import os

os.system("cls || clear")

media: float = 0
soma: float = 0

print("=== Solicitando dados === \n")
primeiroNumero = float (input("Digite o Primeiro Número: ") )
segundoNumero = float (input("Digite o Segundo Número: ") )
terceiroNumero = float (input("Digite o Terceiro Número: ") )

soma = primeiroNumero + segundoNumero + terceiroNumero
media = (primeiroNumero + segundoNumero + terceiroNumero) / 3

print(f"==== Exibindo Resultados:")
print(f"Primeiro Número: {primeiroNumero}")
print(f"Segundo Número: {segundoNumero}")
print(f"Terceiro Número: {terceiroNumero}")
print(f"Resultado da Soma: {soma}")
print(f"Resultado da média: {media}")

if media < 4:
    print("Reprovado")
elif media < 7:
    print("Recuperação")
else:
    print("Aprovado")    
   
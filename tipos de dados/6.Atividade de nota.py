#Tipagem dinâmica
import os

os.system("cls || clear")

print("=== Solicitando dados === \n")
nome = str (input("Digite o nome: ")) 
idade = int (input("Digite a idade: ") )
PrimeiraNota = float (input("Digite a sua Primeira Nota: ") )
SegundaNota = float (input("Digite a sua Segunda Nota: ") )

media = (PrimeiraNota + SegundaNota) / 2

print(f"==== Exibindo Resultados:")
print(f"Primeira Nota: {PrimeiraNota}")
print(f"Segunda Nota: {SegundaNota}")
print(f"resultado da média: {media}")

#Tipagem dinâmica
import os

os.system("cls || clear")

media: float = 0

print("=== Solicitando dados === \n")
nome = str (input("Digite o nome: ")) 
idade = int (input("Digite a idade: ") )
PrimeiraNota = float (input("Digite a sua Primeira Nota: ") )
SegundaNota = float (input("Digite a sua Segunda Nota: ") )
TerceiraNota = float (input("Digite a sua Terceira Nota: ") )

media = (PrimeiraNota + SegundaNota + TerceiraNota) / 3


print(f"==== Exibindo Resultados:")
print(f"Primeira Nota: {PrimeiraNota}")
print(f"Segunda Nota: {SegundaNota}")
print(f"Terceira Nota: {TerceiraNota}")
print(f"resultado da média: {media}")

if media < 5:
    print("Reprovado")
elif media < 7:
    print("Recuperação")
else:
    print("Aprovado")
print(f"FIM")
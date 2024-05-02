import os

os.system("cls || clear")

multiplicacao = 0
numero: int

numero = int (input("Digite um número: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

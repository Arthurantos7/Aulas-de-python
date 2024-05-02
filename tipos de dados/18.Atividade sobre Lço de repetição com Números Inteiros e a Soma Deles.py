import os

os.system("cls || clear")

numero = []
soma = 0
for i in range(5):
   numero.append(int(input(f"Digite o {i+1}º número: ")))
   soma+=numero[i]

os.system("cls || clear")
for i in range(5):
   print(f"{i+1}º Número: {numero[i]}")

print("==== SOMA ====")
print(soma)    



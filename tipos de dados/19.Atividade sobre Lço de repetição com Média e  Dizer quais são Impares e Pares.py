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

os.system("cls || clear")
("=== Números Pares ====")
for i in range(1,6):
   if( i % 2 == 0):
      print(f"Números Pares: {i}")


("=== Números impares ====")
for i in range(1,6):
   if(i % 2 != 0):
      print(f"Números Impares: {i}")     






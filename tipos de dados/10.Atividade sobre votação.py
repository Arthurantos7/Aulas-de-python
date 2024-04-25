#Tipagem dinâmica
import os

os.system("cls || clear")

eleitor = 0

print("=== SOLICITANDO DADOS")
idade = int (input("Digite sua idade: "))

if (idade >= 18 and idade <= 65 ):
   print("é obrigado a votar")
else: 
   print("Não é obrigado a votar")
        
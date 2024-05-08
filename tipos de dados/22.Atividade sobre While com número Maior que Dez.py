#Tipagem dinâmica
import os

os.system("clear")

print("==== SOLICITANDO DADOS ====")
nota = float(input("Digite sua nota: "))

while nota < 0 or nota > 10:
    nota = float(input("Digite sua nota: "))
    
print(f"Resultado da sua nota: {nota}")
   
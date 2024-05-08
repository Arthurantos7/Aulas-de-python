#Tipagem dinâmica
import os

os.system("clear")

soma = 0
media = 0

while True:
    primeiraNota = float(input("Digite a Primeira Nota: "))
    if primeiraNota < 0 or primeiraNota > 10:
        print("Nota inválida. A nota deve estar emtre 0 e 10. Por favor, tente novamente")
    else:
        print("Nota válida:", primeiraNota)    
        break

while True:
    segundaNota = float(input("Digite a Segunda Nota: "))
    if segundaNota < 0 or segundaNota > 10:
        print("Nota inválida. A nota deve estar emtre 0 e 10. Por favor, tente novamente")
    else:
        print("Nota válida:", segundaNota)    
        break

soma = primeiraNota + segundaNota
media = (primeiraNota + segundaNota) / 2

print(f"=== EXIBIR RESULTADOS===")
print(f"Primeira Nota: {primeiraNota}")
print(f"Segunda Nota: {segundaNota}")
print(f"Média: {media}")

#Tipagem dinâmica
import os

os.system("clear")
contadorNotas = 1
soma = 0

while True:
        nota = float(input(f"Digite uma nota: "))
        resposta = input(f"Deseja inserir mais uma nota? ")

        resposta = resposta.upper()
       
        contadorNotas += 1
        soma += nota
        
        if resposta == "N":
            break

media = soma / contadorNotas

print(f"Média: ({media}")

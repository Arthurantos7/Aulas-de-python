#Tipagem dinâmica
import os

os.system("clear")
contador = 0
soma = 0
opcao = "S"

nota = float(input(f"Digite uma nota: "))
soma += nota
contador += 1
while (opcao == "S"):
    print(f"S -Para inserir mais uma nota ")
    print(f"P -Para ver quantas notas foream inseridas ")
    print(f"N -Para calcular a média ")
    opcao = str(input(f"Digite a letra da opçâo desejada:  "))
    opcao = opcao.upper()
       
        
    if (opcao == "N"):
        media = soma / contador
        print(f"Média: {media}")
        break
    if (opcao == "P"):
        print(f"Quantidades de notas inseridas {contador}")
        break
    if (opcao == "S"):
        nota = float(input(f"Digite a próxima nota: "))
        soma += nota
        contador += 1

    if (opcao != "S" and opcao != "P" and opcao != "N"):
        print(f"Opção inválida")
        opcao = "S"
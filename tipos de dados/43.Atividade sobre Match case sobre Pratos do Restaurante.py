import os
import sys
import time

os.system("clear")
#inicializando variável
diaDasemana = 0

# Solicitar dados para o usuário


while True: 
    os.system("clear")
    print("=== MENU ====")
    print("1 /t Picanha /t 25,00R$")
    print("2 /t Lasanha /t 20,00R$")
    print("3 /t Strogonoff /t 18,00R$")
    print("4 /t Bife Acebolado /t 15,00R$")
    print("5 /t Pão com Ovo /t 5,00R$")
    opcao =int(input("Digite o número correspondente ao prato desejado: "))


    match(opcao):
        case 1:
            os.system("clear")
            print("Prato Desejado: Picanha ")
            break       
        case 2:
            os.system("clear")
            print("Prato Desejado: Lasanha")
            break
        case 3:
            os.system("clear")
            print("Prato Desejado: Strogonoff")
            break
        case 4:
            os.system("clear")
            print("Prato Desejado: Bife Acebolado")
            break
        case 5:
            os.system("clear")
            print("Pão com Ovo")
            break
        case _:
            input("Prato inválido")
            
    
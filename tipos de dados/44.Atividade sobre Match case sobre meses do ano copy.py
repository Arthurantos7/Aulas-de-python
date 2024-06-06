import os
import sys
import time

os.system("clear")
#inicializando variável
diaDasemana = 0

# Solicitar dados para o usuário


while True: 
    os.system("clear")
    opcao =int(input("Digite o número correspondente ao mês desejado: "))


    match(opcao):
        case 1:
            os.system("clear")
            print("Janeiro")
            break       
        case 2:
            os.system("clear")
            print("Fevereiro")
            break
        case 3:
            os.system("clear")
            print("Março")
            break
        case 4:
            os.system("clear")
            print("Abril")
            break
        case 5:
            os.system("clear")
            print("Maio")
            break
        
        case 6:
            os.system("clear")
            print("Junho")
            break
        case 7:
            os.system("clear")
            print("Julho")
            break
        
        case 8:
            os.system("clear")
            print("Agosto")
            break
        
        case 9:
            os.system("clear")
            print("Setembro")
            break
        case 10:
            os.system("clear")
            print("Outubro")
            break
        case 11:
            os.system("clear")
            print("Novembro")
            break
        case 12:
            os.system("clear")
            print("Dezembro")
            break
        case _:
            input("Mês inválido")
            
    
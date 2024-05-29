import os
import sys
import time

os.system("clear")
#inicializando variável
diaDasemana = 0

# Solicitar dados para o usuário

while True: 
    opcao = int(input("Digite um Dia da semana: "))

    match(opcao):
        case 1:
            resultado =  ("Domingo: Final de Semana")
            break       
        case 2:
            resultado = ("Segunda: Dia útil")
            break
        case 3:
            resultado = ("Terça: Dia útil")
            break
        case 4:
            resultado = ("Quarta: Dia útil")
            break
        case 5:
            resultado = ("Quinta: Dia útil")
            break
        case 6:
            resultado = ("Sexta: Dia útil")
            break
        case 7:
            resultado = ("Sábado: Fim de Semana")
            break
        case _:
            os.system("clear")
            print("Dia inválido")
            operador = input("Digite um Dia da semana: ")
            

print(f"Resultado: {resultado}")        
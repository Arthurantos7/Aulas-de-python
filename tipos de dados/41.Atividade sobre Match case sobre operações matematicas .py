import os
import sys
import time

os.system("clear")
#inicializando variável
resultado = 0

# Solicitar dados para o usuário
a = int(input("Digite o primeiro número: "))
operador = input("Digite o operador: + - * /: ")
b = int(input("Digite o segundo número: "))

while (resultado == 0):

    match(operador):
        case '+':
            resultado = a + b
        
        case '-':
            resultado = a - b
        
        case '*':
            resultado = a * b
        
        case '/':
            resultado = a / b
        
        case _:
            os.system("clear")
            print("Operador inválido")
            operador = input("Digite o operador: + - * /: ")

print(f"Resultado: {resultado}")        
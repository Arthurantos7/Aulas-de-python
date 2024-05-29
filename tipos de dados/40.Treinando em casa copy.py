import os
import sys
import time

os.system("clear")
homensSalarios5k = 0
mediaSalarios = 0
somaSalarios = 0
homens = 0
quantidadeSalario = 0
quantidadeSalario5k = 0

while True:
    opcao = float(input(f"Digite  Salario Recebido: "))
    match(opcao):

        salario = float(input(f"Digite o Salario Recebido: "))

    somaSalarios += salario
    quantidadeSalario += 1

    if salario >= 5000:
        homensSalarios5k += 1

    if quantidadeSalario != 0:
        mediaSalarios = somaSalarios / quantidadeSalario

    os.system("clear")
    print(f"Homens com Salário 5k: {homensSalarios5k}")        
    print(f"Homens com Salário Abaixo de 5K: {homens}")        







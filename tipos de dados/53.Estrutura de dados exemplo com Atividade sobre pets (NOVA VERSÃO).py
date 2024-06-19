import  os
import sys
import time
from  dataclasses import dataclass

def dados():
    os.system("clear")
    print("===== DADDOS DOS IMPOSTOS=====")
    
def inss(n1):
    if(n1 <= 1100):
        resultadoInss = n1 * 0.075
    elif(n1 <= 2203.48):
        resultadoInss = n1 * 0.09
    elif(n1 <= 3305.22):
        resultadoInss = n1 * 0.12
    elif(n1 <= 6433.57):
        resultadoInss = n1 * 0.14
    else:
        resultadoInss = n1 - (n1 - 854.36)
    return resultadoInss
    
def irrf(n1):
    if(n1 <= 2258.2):
        resultadoIrrf = 0
    elif(n1 <= 2826.65):
        resultadoIrrf = n1 * 0.075
    elif(n1 <= 3751.05):
        resultadoIrrf = n1 * 0.15
    elif(n1 <= 4664.68):
        resultadoIrrf = n1 * 0.225
    else:
        resultadoIrrf = n1 * 0.275
    return resultadoIrrf
    
def transporte(n1):
    resultadoTransporte = n1 * 0.06
    return resultadoTransporte
    
def refeicao(n1):
    resultadoRefeicao = n1 * 0.2
    return resultadoRefeicao

descontoTransporte = 0  

dados()
matricula = input("Digite sua matricula: ")
senha = int(input("Digite sua senha: "))

while True:
    salario = int(input("Digite seu salario base: "))
    if salario < 1:
        input("Tente novamente(PRESS ENTER)")
    else:
        break
while True:    
    transporteValor = input("Deseja receber vale transporte?(sim ou não): ")
    if (transporteValor == "sim"):
        descontoTransporte = transporte(salario)
        break
    if (transporteValor == "não"):
        break
    if(transporteValor != "não" and transporteValor != "sim"):
        input("Tente novamente(PRESS ENTER)")

refeicaoValor = float(input("Digite o valor do seu vale refeição: "))

descontoInss = inss(salario)
descontoIrrf = irrf(salario)
descontoRefeicao = refeicao(refeicaoValor)
calculo =  descontoRefeicao + descontoTransporte + 150 + descontoInss + descontoIrrf  
salarioLiquido = salario - calculo


print(f"Salario Liquido: {salarioLiquido: .2f}")
print(f"Refeição: {refeicaoValor}")
print(f"Plano de saúde: {planoSaude}")
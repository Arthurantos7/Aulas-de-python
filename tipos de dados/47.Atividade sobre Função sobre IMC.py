import os
import sys
import time

# Função sem retorno.
def logoSenai():
    os.system("clear")
    print("=== SENAI === ")

def calculosImc(n1, n2):
    imc= n1 / (n2 * n2)
    
    print(f"IMC: {imc: .1f}")
    
    # Adicionando os dados às listas
    if(imc < 18.5):
        print("Abaixo do Peso")
    if(imc >= 18.5 and imc < 25):
        print("Peso Normal")
    if(imc >= 25 and imc < 30):
        print("Sobrepeso")
    if(imc >= 30 and imc < 35):
        print("Obesidade Grau 1")
    if(imc >= 35 and imc < 40):
        print("Obesidade Grau 2")
    if(imc >= 40):
        print("Obesidade Grau 3 (mórbida)")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []
# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input(f"Digite o sobrenome do usuário: ")
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)


# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"==== {i+1}º DADOS ====")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    
    calculosImc(pesos[i], alturas[i])



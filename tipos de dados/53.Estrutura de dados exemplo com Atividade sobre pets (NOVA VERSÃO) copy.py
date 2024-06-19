import os
import math
import sys
import time
from dataclasses import dataclass
def cabecalho():
    os.system("clear")
    print("=== DADOS === ")

def dadosSaude():
    os.system("clear")
    print("=== DADOS DE SAÚDE ===")

def calcularIMC(peso, altura):
    return peso / math.pow(altura, 2)

def situacaoIMC(imc):
    if imc < 18.5:
        print("Muito magro")
    if imc >= 18.5 and imc < 25:
        print("Peso normal")
    if imc >= 25 and imc < 30:
        print("Sobrepeso")
    if imc >= 30 and imc < 35:
        print("Obesidade grau I")
    if imc >= 35 and imc < 40:
        resultado ="Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"

    return resultado

class DadosUsuario:
    def __init__(self,nome_do_usuario: str,sobrenome_do_usuario: str, nomeCompleto: str, idade_do_usuario, altura_do_usuario, peso_do_usuario,imc, situacao):

        self.nome = nome_do_usuario
        self.sobrenome = sobrenome_do_usuario
        self.nomeCompleto = nome_do_usuario + sobrenome_do_usuario
        self.idade = idade_do_usuario
        self.altura = altura_do_usuario
        self.peso = peso_do_usuario
        self.imcs = imc
        self.situacaoIMC = situacao

dadosDosUsuarios = []
nomeCompleto = str

while True:
    dadosSaude()
    nome_do_usuario = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    if nome_do_usuario.lower() == 'sair':
        break
    
    sobrenome_do_usuario = input("Digite o sobrenome do usuário: ")
    idade_do_usuario = int(input("Digite a idade do usuário: "))
    altura_do_usuario = float(input("Digite a altura do usuário (em metros): "))
    peso_do_usuario = float(input("Digite o peso do usuário (em quilogramas): "))
    
    imc = calcularIMC(peso_do_usuario, altura_do_usuario)
    situacao = situacaoIMC(imc)
    dadosDosUsuarios.append(DadosUsuario(nome_do_usuario, sobrenome_do_usuario, nomeCompleto, idade_do_usuario, altura_do_usuario, peso_do_usuario, imc, situacao))

dadosSaude()
print("\nDados dos usuários: \n")
for i, j in enumerate(dadosDosUsuarios):
    print(f"====== {i+1} DADOS ======")
    print(f"Usuário {i+1}:")
    print(f"Nome: {j.nome}")
    print(f"Sobreome: {j.sobrenome}")
    print(f"Nome completo: {j.nomeCompleto}")
    print(f"Idade: {j.idade}")
    print(f"Altura: {j.altura} metros")
    print(f"Peso: {j.peso: .1f} quilogramas")
    print(f"IMC: {j.imcs: .1f}")
    print(f"Situação: {j.situacaoIMC}")
    print()
    


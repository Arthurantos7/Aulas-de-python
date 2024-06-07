import os
import sys
import time

os.system("clear")
prato = []
valorPrato = 0
repetirEscolha = 0
formaPagamneto = 0
contadorPrato = 0
subtotal = 0
while True:
    os.system("clear")
    print("=== MENU ===")
    print("1 /t Bolo de Chocolate /t R$ 15,00")
    print("2 /t Macarrão Ao vivo /t R$ 10,00")
    print("3 /t Bauru /t R$ 5,00")
    print("4 /t Pastel de Forno /t R$ 5,00")
    print("5 /t Brigadeiro /t R$ 1,00")
    print("6 /t Churros /t R$ 1,50")
    print("7 /t Fanta /t R$ 3,50")

    opcao = int(input("Digite o prato desejado: "))
        
    while opcao < 1 and opcao > 7:
        input("opção inválida")
        os.system("clear")
        print("=== MENU ===")
        print("1 /t Bolo de Chocolate /t R$ 15,00")
        print("2 /t Macarrão Ao vivo /t R$ 10,00")
        print("3 /t Bauru /t R$ 5,00")
        print("4 /t Pastel de Forno /t R$ 5,00")
        print("5 /t Brigadeiro /t R$ 1,00")
        print("6 /t Churros /t R$ 1,00")
        print("7 /t Fanta /t R$ 3,00")
        
        opcao = int(input("Digite o prato desejado: "))
    
    match(opcao):
        
        case 1:
            contadorPrato += 1
            subtotal += 15
            prato.append("1 /t Bolo de Chocolate /t R$ 15,00")
        case 2:
            contadorPrato += 1
            subtotal += 10
            prato.append("2 /t Macarrão Ao vivo /t R$ 10,00")
            
        case 3:
            contadorPrato += 1
            subtotal += 5
            prato.append("3 /t Bauru /t R$ 10,00")
            
            
        case 4:
            contadorPrato += 1
            subtotal += 5
            prato.append("4 /t Pastel de Forno /t R$ 5,00")
            
            
        case 5:
            contadorPrato += 1
            subtotal += 1
            prato.append("5 /t Brigadeiro /t R$ 1,00")
            
            
        case 6:
            contadorPrato += 1
            subtotal += 1
            prato.append("4 /t Churros /t R$ 1,00")
            
            
        case 7:
            contadorPrato += 1
            subtotal += 3
            prato.append("4 /t Fanta /t R$ 3,00")
            
            
    os.system("clear")
    repetirEscolha = int(input("Deseja pedir outro prato (1 pra SIM | 0 pra NÂO): "))
    
    if repetirEscolha == 0:
        while True:
            os.system("clear")
            formaPagamento = int(input("Digite a forma de pagamento desejada(1 pra á vista | 2 pra parcelado): "))
            
            if (formaPagamento == 1):
                desconto = subtotal * 0.10
                valorFinal = subtotal - desconto
                break
            if (formaPagamento == 2):
                quantidadeParcela = int(input("Digite a quantidade de parcelas desejadas: "))
                valorParcela = subtotal / quantidadeParcela
                taxa = subtotal * 0.10
                valorFinal = subtotal + taxa
                break
            if (formaPagamento != 1 and formaPagamento != 2):
                input("Opção inválida")
        break    
os.system("clear")
print("== Pratos selecionados ==")    
for i in range(contadorPrato):
    print(prato[i])
print("== Pratos selecionados ==")

if formaPagamento == 1: 
    print(f"Forma de Pagamneto desejada: á vista")
    print(f"Valor do Desconto: {desconto: .2f}")
    print(f"Valor do subtotal: {subtotal: .1f}")
    print(f"Valor total: {valorFinal: .1f}")
    
    
if formaPagamento == 2:
    print(f"Forma de Pagamneto desejada: á prazo")
    print(f"Quantidade de Parcelas: {quantidadeParcela}")
    print(f"Valor por Parcela: {valorParcela: .1f}")
    print(f"Valor da taxa: {taxa: .1f}")
    print(f"Valor do subtotal: {subtotal: .1f}")
    print(f"Valor total: {valorFinal: .1f}")
    
        
        
        


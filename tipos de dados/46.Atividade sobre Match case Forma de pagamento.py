import os
import sys
import time

os.system("clear")

valorProduto = float(input("Digite o valor do produto: "))

while True:
    
    formaPagamento = input("Digite a forma de pagamneto desejada: ")

    if formaPagamento != "avista" and formaPagamento != "credito":
        input("Opção inválida")

    else:
        break


if formaPagamento == "avista":
    valorFinal = valorProduto - (valorProduto * 0.10) 
    print(f"Valor do produto: {valorProduto}")
    print(f"Valor Final: {valorFinal}")
    print(f"Forma de Pagamento: {formaPagamento}")
    print(f"Valor do Desconto: {valorProduto * 0.10}")

if formaPagamento == "crédito":
    parcelas = input("Digite a quantidade de parcela:")
    valorFinal = valorProduto / parcelas
    print(f"Valor do produto: {valorProduto}")
    print(f"Valor Final: {valorProduto}")
    print(f"Quantidade de  Parcelas: {parcelas}")
    print(f"Forma de pagamento {formaPagamento}")
    print(f"Valor por Parcela: {valorFinal}")

    


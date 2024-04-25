#Tipagem dinâmica
import os

os.system("cls || clear")

print("=== SOLICITANDO DADOS")
nomeProduto = (input("Digite o nome do produto: "))
quantidadeAdquirida = int (input("Digite a quantatidade Adquirida: "))
precoUnitario = float (input("Digite o preço únitario do produto: "))

total =  quantidadeAdquirida * precoUnitario

if quantidadeAdquirida <= 5:
   totalDesconto = total - (total * 0.02)
elif quantidadeAdquirida <= 10:
   totalDesconto = total - (total * 0.03)
else:
   totalDesconto = total - (total * 0.05)

print(f"nome do produto: {nomeProduto}")
print(f"quantidade adquirida: {quantidadeAdquirida}")
print(f"Preço únitario: {precoUnitario}")
print(f"Total de Desconto: {totalDesconto}")
print(f"Total sem Desconto: {total}")


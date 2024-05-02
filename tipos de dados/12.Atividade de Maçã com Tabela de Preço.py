import os 

os.system("cls || clear")

print("\n=== Solicitando dados ==")
pesoMorango = float(input("Digite o peso dos morangos (em kg): "))
pesoMaca = float(input("Digite o peso de maçãs (em kg): "))

if pesoMorango < 5:
    precoMorango = 2.50
else :
    precoMorango = 2.20

if pesoMaca < 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

pesoTotal = pesoMorango + pesoMaca
subtotal  = (precoMorango + pesoMorango) + (precoMaca + pesoMaca )

if pesoTotal > 8 or subtotal > 25:
    desconto = subtotal * 0.10

totalPagar = subtotal - desconto

print("\n=== Exibindo resultados ===")
print(f"Peso de morangos (em kg): {pesoMorango}")
print(f"Peso de maçãs (em kg): {pesoMaca}")
print(f"Soma de pesos (em kg): {pesoTotal}")
print(f"Subtotal: R$ {subtotal: .2f}")
print(f"Desconto: R$ {desconto: .2f}")
print(f"Total a pagar: R$ {desconto: .2f}")


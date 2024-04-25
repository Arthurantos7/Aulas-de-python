#Tipagem dinâmica
import os

os.system("cls || clear")

print("=== Solicitando dados === \n")
email = str (input("Digite o email: ")) 
senha = str (input("Digite a senha: "))

if (email == "thur@gmail.com" and senha == "999"):
   print("Bem Vindo") 
else:
   print("login ou senha incorreta")   


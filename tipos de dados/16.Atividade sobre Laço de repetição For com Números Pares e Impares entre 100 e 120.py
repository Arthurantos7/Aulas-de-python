import os

os.system("cls || clear")

print("=== Números pares===")
for i in range(100,120):
   if (i % 2 == 0): 
    print(f"Números Pares: {i}")

print("===Números impares===")
for i in range(100,120):
  if( i % 2 != 0):
      print(f"Números impares: {i}")
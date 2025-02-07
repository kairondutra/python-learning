# **Exercícios:**

# 1. Escreva um programa que verifique se um número é par ou ímpar.

numero = int(input("Escreva um número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# 2. Crie um programa que peça a idade do usuário e informe se ele é maior de idade.

idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")

# 3. Faça um programa que leia três números e imprima o maior deles.

a = int(input("Escreva o primeiro número: ")) 
b = int(input("Escreva o segundo número: ")) 
c = int(input("Escreva o terceiro número: ")) 

if a > b and a > c:
    print(f"{a} é o maior número!")
elif b > a and b > c:
    print(f"{b} é o maior número!")
else:
    print(f"{c} é o maior número!")


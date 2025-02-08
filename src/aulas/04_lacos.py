# **Exercícios:**

# 1. Escreva um programa que imprima todos os números pares de 1 a 20.

print("Números pares de 1 a 20:")

aux = 0
while aux <= 20:
    if aux % 2 == 0:
        print(aux)
    aux+=1

# 2. Crie um programa que calcule o fatorial de um número fornecido pelo usuário.

numero = int(input("Informe um número para o calculo de fatorial: "))
if numero < 0:
    print("Fatorial não está definido para números negativos.")

resultado = 1
for i in range(1, numero + 1):
    resultado *= i

print(f"O fatorial de {numero} é igual a: {resultado}")


# 3. Faça um programa que simule um contador regressivo de 10 a 0.

for n in range(10,-1,-1):
    print(n ,end=" ")

# Exercícios Adicionais

# 4. Escreva um programa que imprima todos os números ímpares de 1 a 30.

print("Números ímpares de 1 a 30:")
for i in range(1,31,2):
    print(i)
print()

# 5. Crie um programa que calcule a soma de todos os números de 1 a 100.

soma = 0
for num in range(101):
    soma += num
print(f"a soma dos primeiros cem números é {soma}")

# 6. Faça um programa que imprima a tabuada de um número fornecido pelo usuário

numero = int(input("Informe um número para ver sua tabuada: "))
print(f"Tabuada do {numero}:")
for n in range(1,11):
    print(f"{n} x {numero} = {n*numero}")

# 7. Escreva um programa que imprima todos os múltiplos de 3 entre 1 e 50.

print("Múltiplos de 3 entre 1 e 50")
for n in range(51):
    if n % 3 == 0:
        print(f"{n}")

# 8. Crie um programa que calcule a média de 5 números fornecidos pelo usuário.

soma = 0
for i in range(1, 6):
    numero = float(input(f"Informe o {i}° número: "))
    soma += numero
media = soma / 5
print(f"A média dos números fornecidos é {media:.2f}.")

# 9. Faça um programa que imprima a sequência de Fibonacci até o 10º termo.

print("Sequência de Fibonacci (10 termos):")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

# 10. Escreva um programa que verifique se um número fornecido pelo usuário é primo.

numero = int(input("Informe um número para verificar se é primo: "))
if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é primo.")
            break
    else:
        print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")


# 11. Crie um programa que simule um cronômetro de segundos, contando de 1 a 60.
import time

for sec in range(1, 61):
    print(f"\r{sec} ", end="", flush=True)
    time.sleep(1)

print("\nFim!")

# 12. Faça um programa que imprima todos os divisores de um número fornecido pelo usuário.

num = int(input("Informe o número: "))
print(f"Os divisores de {num} são:", end=" ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=", " if i != num else "\n") 

# 13. Escreva um programa que calcule o produto de todos os números de 1 a 10.

produto = 1
for n in range(1,11):
    produto *= n
print(f"O produto de todos os números de 1 a 10 é {produto}.")

# 14. Crie um programa que imprima um triângulo numérico.

altura = int(input("Informe a altura do triângulo: "))
for i in range(1, altura + 1):
    print(" ".join([str(i)] * i))  # Usando join() para controle de espaçamento
# **Exercícios:**
# 1. Escreva um programa que calcule a média de três notas fornecidas pelo usuário.

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

media = (a+b+c)/3
print(f"A média dos valores fornecidos é {media}")


# 2. Crie um programa que converta uma temperatura em Celsius para Fahrenheit.
celcius = float(input("Informe a temperatura em Celcius para a conversão: "))
fahrenheit = (celcius * 9/5) + 32
print(f"A temperatura em Fahrenheit é {fahrenheit}")


# 3. Faça um programa que leia um número inteiro e imprima seu quadrado e sua raiz quadrada.
numero = int(input("Informe um número inteiro: "))
print(f"o quadrado do número {numero} é {numero**2} e sua raiz é {numero**0.5}")

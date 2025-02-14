# **Exercícios:**
# 1. Crie uma função que receba dois números como parâmetros e retorne a soma deles.

def soma(a,b):
    return a+b
print(soma(1,3))

# 2. Escreva uma função que calcule o fatorial de um número fornecido pelo usuário.

def factorial(n):
    if n < 0:
        return "Fatorial não está definido para números negativos."
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

numero = int(input("Informe um número para o cálculo de fatorial: "))
print(f"O fatorial de {numero} é igual a: {factorial(numero)}")

# 3. Faça uma função que receba uma lista de números e retorne o maior valor da lista.

def maior(*numeros):
    if not numeros:
        return "Lista vazia, não há maior valor."
    
    maior = numeros[0]
    for num in numeros:
        if num > maior:
            maior = num
    return maior

print(maior(1,2,3,4,5,6))

# 4. Crie uma função que verifique se um número é par ou ímpar e retorne uma mensagem indicando o resultado.

def par_impar(n):
    return "par" if n % 2 == 0 else "ímpar"

print(par_impar(7))

# 5. Escreva uma função que calcule a área de um círculo dado o raio.

import math

def area_circulo(raio):
    if raio < 0:
        return "O raio não pode ser negativo."
    return math.pi * (raio**2)

# 6. Crie uma função que receba uma lista de números e retorne a soma deles.

def somatorio(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

print(somatorio(1,2,3,4,5))

# 7. Faça uma função que verifique se uma palavra é um palíndromo.

import string

def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation)) 
    
    if texto == texto[::-1]:
        return "É palíndromo!"
    else:
        return "Não é um palíndromo!"

texto_usuario = input("Escreva uma palavra/texto para verificação: ")
resultado = palindromo(texto_usuario)
print(resultado)
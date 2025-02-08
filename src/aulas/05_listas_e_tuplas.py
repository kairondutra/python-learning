# Exercícios

# 1. Crie uma lista de números e imprima o maior e o menor valor.

lista = [1, 2, 9, 3, 4, 5]
maior, menor = lista[0], lista[0]

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]

print(f"O maior número da lista é {maior} e o menor é {menor}")

# 2. Escreva um programa que remova duplicatas de uma lista.

lista = [1, 1, 2, 3, 9, 6, 9, 7, 5, 8, 4, 5]
nova_lista = []

for i in lista:
    if i not in nova_lista:
        nova_lista.append(i)

print(f"{nova_lista}")

# 3. Faça um programa que inverta a ordem dos elementos de uma lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.reverse()

print(f"{lista}")

# Exercícios Extras

# Crie uma lista com 5 números inteiros e exiba o terceiro número da lista.

lista = [1,2,3,4,5,6]
print(lista[2])

# Escreva um programa que peça ao usuário para digitar 3 frutas e as adicione a uma lista. Em seguida, exiba a lista completa.

frutas = []
for f in range(3):
    fruta = input("Digite o nome de uma fruta: ")
    frutas.append(fruta)
    print(f"a fruta '{fruta}' foi adicionada!")
print(f"Lista de Frutas: {frutas}")

# Faça um programa que remova o último elemento de uma lista e exiba a lista atualizada.

lista = ["Brasil", "Argentina", "Bruxelas", "Espanha", "Canada", "Chile", "India"]
print(f"Lista original: {lista} ")

lista.pop()
print(f"Lista sem o último elemento: {lista}")

# Ordene uma lista de números fornecida pelo usuário em ordem crescente e exiba o resultado.

lista_desordenada = []

while True:
    elemento = input("Digite um elemento para adicionar à lista (ou 'q' para sair): ").strip().lower()

    if elemento == "q":
        break
    lista_desordenada.append(elemento)

lista_ordenada = sorted(lista_desordenada)

print("\nResultados:")
print(f"Lista desordenada: {lista_desordenada}")
print(f"Lista ordenada: {lista_ordenada}")



# Exercícios sobre Tuplas:
# Crie uma tupla com 4 números inteiros e exiba o segundo número.

tupla = (1,2,3,4)
print(f"Tupla: {tupla}")
print(f"Segundo elemento: {tupla[1]}")

# Escreva um programa que conte quantas vezes o número 5 aparece em uma tupla fornecida pelo usuário.

numeros=[]

while True:
    elemento = input("Digite um número (ou uma letra para sair): ").strip().lower()

    if elemento.isdigit():
        numeros.append(int(elemento))
    elif elemento.isalpha():
        print("Saindo...")
        break
    else:
        print("Entrada inválida! Digite apenas números ou letras para sair.")

tupla_numeros = tuple(numeros)
quantidade_5 = tupla_numeros.count(5)

print(f"Tupla criada: {tupla_numeros}")
print(f"O número 5 apareceu {quantidade_5} vezes.")

# Faça um programa que encontre o índice do valor "azul" 
# em uma tupla de cores ("vermelho", "verde", "azul").

cores = ("vermelho", "verde", "azul")

indice_azul = cores.index("azull")
print(f"A cor 'azul' está no índice {indice_azul}.")

# Explique, em suas palavras, a principal diferença entre listas e tuplas.

'''
A principal diferença entre listas e tuplas no Python está na mutabilidade. 
Enquanto as listas são estruturas de dados flexíveis, que permitem a adição, 
remoção e modificação de elementos, as tuplas são imutáveis, ou seja, seus 
elementos não podem ser alterados depois de criados.
'''
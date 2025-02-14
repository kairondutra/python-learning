# **Exercícios:**
# 1. Crie um dicionário com nomes de alunos e suas notas, e imprima a média das notas.

alunos_notas = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 7.5,
    "Ana": 10.0,
    "Lucas": 6.5
}

soma_notas = sum(alunos_notas.values())
media_notas = soma_notas / len(alunos_notas)
print(f"{soma_notas}\n{media_notas:.2f}")

# 2. Escreva um programa que conte a frequência de palavras em uma frase usando um dicionário.

frase = input("Escreva a frase: ")
palavras = frase.lower().split()

frequencia = {}

for palavra in palavras:
    palavra = palavra.strip(".,!?;:\"'()[]{}")

    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("\nFrequência de palavras:")
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")

# 3. Crie um dicionário que represente informações de # um livro (título, autor, ano de publicação) e exiba cada informação separadamente.

livro = {
    "Titulo":"A Guerra dos Tronos",
    "Autor": "George R.R. Martin",
    "Ano de publicação": 1996
}

print("Informação do Livro: ")
print(f"Titulo: {livro['Titulo']}")
print(f"Autor: {livro['Autor']}")
print(f"Ano de publicação: {livro['Ano de publicação']}")

# 4. Escreva um programa que peça ao usuário para digitar o nome e a idade de uma pessoa e armazene essas informações em um dicionário. Em seguida, exiba o dicionário completo.

perguntas = {
    "Nome": "Digite seu nome: ",
    "Idade": "Digite sua idade: "
}

dados_usuario = {}

for chave, pergunta in perguntas.items():
    dados_usuario[chave] = input(pergunta)

print("\nDicionário com os dados do usuário:")
print(dados_usuario)

# 5. Faça um programa que remova uma chave específica de um dicionário fornecido pelo usuário.

dados = {}
while True:
    chave = input("Digite a chave (ou 'sair' para finalizar): ")
    if chave.lower() == "sair":
        break
    else:
        valor = input("Digite o valor: ")
        dados[chave] = valor

print(f"Dicionário Atual: {dados}")
chave_remover = input("\nDigite a chave que deseja remover: ")

if chave_remover in dados:
    del dados[chave_remover]
    print("\nChave removida com sucesso!")
else:
    print("\nErro: Chave não encontrada.")

print("\nDicionário atualizado:", dados)

# 6. Use o método get() para acessar um valor em um dicionário. Se a chave não existir, exiba uma mensagem personalizada.

dict = {
    "Nome": "Kairon",
    "idade": "25"
}

print(dict.get("Altura", "Valor não encontrado!"))

# 7. Faça um programa que remova elementos duplicados de uma lista usando conjuntos.

lista = [1,2,2,3,3,4]
print(set(lista))

# 8. Crie um conjunto com números inteiros e remova os números pares.

inteiros = {1,2,3,4,5,6,7,8,9,10}
for num in list(inteiros):
    if num % 2 == 0:
        inteiros.remove(num)
print(inteiros)

# 9. Escreva um programa que receba duas listas de números e crie conjuntos a partir delas. Em seguida, exiba a união, a interseção e a diferença entre os conjuntos.

lista_a = [1,2,3,4,5]
lista_b = [4,5,6,7,8]

conjunto_a = set(lista_a)
conjunto_b = set(lista_b)

uniao = conjunto_a | conjunto_b
intersecao = conjunto_a & conjunto_b
diferenca = conjunto_a - conjunto_b

print(f"União: {uniao}\nInterseção: {intersecao}\nDiferença: {diferenca}")

# 10. Faça um programa que verifique se dois conjuntos têm elementos em comum.

conjunto1 = {1,2,3,4,5}
conjunto2 = {3,4,"5",1}

if conjunto1 & conjunto2:
    print("os conjuntos possuem valores em comum.")
else:
    print("os conjuntos NÃO possuem valores em comum.")

# 11. Use um conjunto para eliminar duplicatas de uma lista fornecida pelo usuário.

numeros = []

while True:
    numero = input("Informe um número (letra para sair): ")
    if numero.isalpha():
        break
    elif numero.isdigit():
        numeros.append(int(numero))
    else:
        print("Valor Inválido.")
        
lista_sem_duplicatas = set(numeros)
print(lista_sem_duplicatas)
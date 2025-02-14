# 1. Escreva um programa que leia um arquivo de texto e imprima seu conteúdo.

with open("novo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


# 2. Crie um programa que grave uma lista de nomes em um arquivo.
nomes = ["Ana", "Bruno", "Carla", "Daniel", "Elena", "Felipe", "Gabriela", "Henrique", "Isabela", "João"]

with open("arquivo_teste.txt", "w", encoding="utf-8") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")
    print("Nomes escritos com sucesso!")


# 3. Faça um programa que conte o número de linhas de um arquivo.

with open("arquivo_teste.txt", "r", encoding="utf-8") as ar:
    linhas = len(ar.readlines())
    print(f"o arquivo possui {linhas} linhas.")


# 4. Faça um programa que leia um arquivo linha por linha e exiba cada linha numerada.

with open("arquivo_teste.txt", "r", encoding="utf-8") as ar:
    linhas = ar.readlines()
    numero = 1
    for linha in linhas:
        print(f"{numero}: {linha}", end='')
        numero += 1


# 5. Escreva um programa que copie o conteúdo de um arquivo para outro arquivo. 

with open("arquivo_teste.txt", "r", encoding="utf-8") as arquivo:
    conteudo_arquivo = arquivo.read() 

with open("new.txt", "w", encoding="utf-8") as destino:
    destino.write(conteudo_arquivo) 


# 6. Crie um programa que concatene o conteúdo de dois arquivos em um terceiro arquivo. 

with open("docs_auxiliares/primeiro.txt", "r", encoding="utf-8") as primeiro:
    primeiro_conteudo = primeiro.read() 
    print(primeiro_conteudo)
    # conteúdo do arquivo 1: abc

with open("docs_auxiliares/segundo.txt", "r", encoding="utf-8") as segundo:
    segundo_conteudo = segundo.read() 
    print(segundo_conteudo)
    # conteúdo do arquivo 2: 123
    
with open("docs_auxiliares/terceiro.txt","w+", encoding="utf-8") as terceiro:
    terceiro.write(primeiro_conteudo + segundo_conteudo)
    terceiro.seek(0)
    print(terceiro.read())
    # resultado: abc123


# 7. Faça um programa que leia um arquivo e conte o número de palavras no conteudo. 

import string

with open("docs_auxiliares/lorem.txt", "r", encoding="utf-8") as primeiro:
    conteudo = primeiro.read().lower()
    conteudo = conteudo.translate(str.maketrans("", "", string.punctuation))
    texto = conteudo.split()
    
    frequencias = {}
    
    for palavra in texto: 
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1
                
    for palavra in sorted(frequencias.keys()):
        print(f"{palavra}: {frequencias[palavra]}")


# 8. Escreva um programa que substitua todas as ocorrências de uma palavra específica 
# em um arquivo por outra palavra. 

with open("docs_auxiliares/lorem.txt", "r") as arquivo_original:
    conteudo = arquivo_original.read()
    print(conteudo)
    
    novo_conteudo = conteudo.replace("lorem", "teste")

with open("docs_auxiliares/lorem.txt", "w") as arquivo_modificado:
    arquivo_modificado.write(novo_conteudo)


# 9. Crie um programa que leia um arquivo CSV (valores separados por vírgula) e 
# exiba seus dados em formato tabular.

with open("docs_auxiliares/example.csv", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        colunas = linha.strip().split(",")
        print("\t".join(colunas))


# 10. Faça um programa que salve um dicionário em um arquivo JSON e 
# depois leia o arquivo para recuperar o dicionário. 

import json

dados = [
    {"Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Bob", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 22, "Cidade": "Belo Horizonte"}
]

with open("dicionario.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)

with open("dicionario.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

print(dados_carregados)

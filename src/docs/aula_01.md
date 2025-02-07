# 📚 Aula 01: Introdução ao Python

Este arquivo contém os comentários explicativos detalhados sobre os exercícios da **Aula 01**, que servirão como anotações para entender o código.

---

## Exercício 1: Imprimir "Olá, Mundo!"

- **Descrição:** Escreva um programa que imprima "Olá, Mundo!" na tela.
- **Função Utilizada:** `print()`
  - A função `print()` exibe valores no console (stdout).
  - Neste exemplo, estamos imprimindo uma string simples.
- **Saída Esperada:**
```cmd
Olá, Mundo!
```
---

## Exercício 2: Cumprimentar o Usuário pelo Nome

- **Descrição:** Crie um programa que pergunte o nome do usuário e o cumprimente com "Olá, [nome]!".
- **Funções Utilizadas:**
- `input()`: Exibe uma mensagem ao usuário e captura a entrada como uma string.
- Declaramos uma variável `nome` para armazenar o valor inserido pelo usuário.
- F-strings (format strings): Permitem interpolar variáveis diretamente na string, tornando o código mais legível.
- **Exemplo de Saída:** 
```cmd
Qual seu nome? Kairon  
Olá, Kairon!
```
---

## Exercício 3: Somar Dois Números Fornecidos pelo Usuário

- **Descrição:** Faça um programa que peça dois números ao usuário e imprima a soma deles.
- **Detalhes Importantes:**
- A função `input()` sempre retorna uma string, então precisamos convertê-la para o tipo desejado.
- **Conversão de Tipos:**
  - `int()`: Para números inteiros (ex.: 5, -10).
  - `float()`: Para números decimais (ex.: 3.14, -0.5).
- Solicitamos dois números ao usuário e convertemos as entradas para inteiros usando `int()`.
- Calculamos a soma dos dois números e exibimos o resultado formatado usando uma f-string.
- **Exemplo de Saída:**  
```cmd
Informe o primeiro número: 5  
Informe o segundo número: 3  
5 + 3 = 8
```
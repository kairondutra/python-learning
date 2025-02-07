# 📚 Aula 03: Estruturas Condicionais

Este arquivo contém os comentários explicativos detalhados sobre os exercícios da **Aula 03**, que servirão como anotações para entender o código.

---

## Exercício 1: Verificar se um Número é Par ou Ímpar

- **Descrição:** Escreva um programa que verifique se um número fornecido pelo usuário é par ou ímpar.
- **Conceitos Utilizados:**
  - Operador `%` (módulo): Retorna o resto da divisão entre dois números.
    - Se o resto da divisão por 2 for `0`, o número é par.
    - Caso contrário, o número é ímpar.
  - Estrutura condicional `if` e `else`.
- **Explicação do Código:**
  - Declaramos uma variável `numero` para armazenar o valor fornecido pelo usuário.
  - Usamos o operador `%` para verificar se o número é divisível por 2.
  - Se a condição `numero % 2 == 0` for verdadeira, o programa imprime "Par".
  - Caso contrário, imprime "Ímpar".
- **Exemplo de Saída:**  
```cmd
Escreva um número: 4  
Par  
```
---

## Exercício 2: Verificar se o Usuário é Maior de Idade

- **Descrição:** Crie um programa que peça a idade do usuário e informe se ele é maior de idade.
- **Conceitos Utilizados:**
- Estrutura condicional `if` e `else`.
- Comparação usando o operador `>=` (maior ou igual).
- **Explicação do Código:**
- Declaramos uma variável `idade` para armazenar o valor fornecido pelo usuário.
- Verificamos se a idade é maior ou igual a 18.
- Se a condição `idade >= 18` for verdadeira, o programa imprime "Maior de idade".
- Caso contrário, imprime "Menor de idade".
- **Exemplo de Saída:**  
```cmd
Informe sua idade: 20  
Maior de idade.  
```
---

## Exercício 3: Encontrar o Maior de Três Números

- **Descrição:** Faça um programa que leia três números e imprima o maior deles.
- **Conceitos Utilizados:**
- Estrutura condicional `if`, `elif` e `else`.
- Operadores lógicos (`and`) para comparar múltiplas condições.
- **Explicação do Código:**
- Declaramos três variáveis (`a`, `b`, `c`) para armazenar os valores fornecidos pelo usuário.
- Comparamos os números usando condições combinadas com o operador `and`:
  - Se `a` for maior que `b` **e** `a` for maior que `c`, então `a` é o maior número.
  - Senão, verificamos se `b` é maior que `a` **e** `b` é maior que `c`.
  - Caso nenhuma das condições acima seja verdadeira, concluímos que `c` é o maior número.
- Usamos f-strings para exibir o resultado formatado.
- **Exemplo de Saída:**  
```cmd
Escreva o primeiro número: 5  
Escreva o segundo número: 12  
Escreva o terceiro número: 7  
12 é o maior número!  
```
---

## Resumo dos Conceitos Aprendidos

1. **Operador `%` (Módulo):**
 - Retorna o resto da divisão entre dois números.
 - Exemplo: `4 % 2 == 0` (par), `5 % 2 != 0` (ímpar).

2. **Estruturas Condicionais:**
 - `if`: Executa um bloco de código se a condição for verdadeira.
 - `elif`: Verifica condições adicionais.
 - `else`: Executa um bloco de código se nenhuma condição anterior for verdadeira.

3. **Operadores de Comparação:**
 - `==`: Igual.
 - `!=`: Diferente.
 - `>`: Maior que.
 - `<`: Menor que.
 - `>=`: Maior ou igual.
 - `<=`: Menor ou igual.

4. **Operadores Lógicos:**
 - `and`: Retorna `True` se todas as condições forem verdadeiras.
 - `or`: Retorna `True` se pelo menos uma condição for verdadeira.
 - `not`: Inverte o valor booleano.


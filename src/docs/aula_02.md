# 📚 Aula 02: Operações Matemáticas e Conversões

Este arquivo contém os comentários explicativos detalhados sobre os exercícios da **Aula 02**, que servirão como anotações para entender o código.

---

## Exercício 1: Calcular a Média de Três Notas

- **Descrição:** Escreva um programa que calcule a média de três notas fornecidas pelo usuário.
- **Funções Utilizadas:**
  - `input()`: Captura a entrada do usuário como uma string.
  - `float()`: Converte a entrada para um número decimal (float).
  - Fórmula da média: `(a + b + c) / 3`.
- **Explicação do Código:**
  - Declaramos três variáveis (`a`, `b`, `c`) para armazenar as notas fornecidas pelo usuário.
  - Convertimos as entradas para números decimais usando `float()`.
  - Calculamos a média dividindo a soma das notas por 3.
  - Usamos uma f-string para exibir o resultado formatado.
- **Exemplo de Saída:**  
```cmd
Informe o valor de a: 7.5  
Informe o valor de b: 8.0  
Informe o valor de c: 6.5  
A média dos valores fornecidos é 7.333333333333333  
```
---

## Exercício 2: Converter Temperatura de Celsius para Fahrenheit

- **Descrição:** Crie um programa que converta uma temperatura em Celsius para Fahrenheit.
- **Fórmula de Conversão:**
- Fahrenheit = `(Celsius * 9/5) + 32`.
- **Funções Utilizadas:**
- `input()`: Captura a entrada do usuário como uma string.
- `float()`: Converte a entrada para um número decimal (float).
- **Explicação do Código:**
- Declaramos uma variável `celcius` para armazenar a temperatura fornecida pelo usuário.
- Convertimos a entrada para um número decimal usando `float()`.
- Aplicamos a fórmula de conversão para calcular a temperatura em Fahrenheit.
- Usamos uma f-string para exibir o resultado formatado.
- **Exemplo de Saída:**  
```cmd
Informe a temperatura em Celcius para a conversão: 25  
A temperatura em Fahrenheit é 77.0
```
---

## Exercício 3: Calcular o Quadrado e a Raiz Quadrada de um Número

- **Descrição:** Faça um programa que leia um número inteiro e imprima seu quadrado e sua raiz quadrada.
- **Funções Utilizadas:**
- `input()`: Captura a entrada do usuário como uma string.
- `int()`: Converte a entrada para um número inteiro.
- Operadores matemáticos:
  - Quadrado: `numero ** 2`.
  - Raiz quadrada: `numero ** 0.5`.
- **Explicação do Código:**
- Declaramos uma variável `numero` para armazenar o valor fornecido pelo usuário.
- Convertimos a entrada para um número inteiro usando `int()`.
- Calculamos o quadrado do número elevando-o à potência de 2 (`** 2`).
- Calculamos a raiz quadrada do número elevando-o à potência de 0.5 (`** 0.5`).
- Usamos uma f-string para exibir os resultados formatados.
- **Exemplo de Saída:**  
```cmd
Informe um número inteiro: 16  
O quadrado do número 16 é 256 e sua raiz é 4.0  
```
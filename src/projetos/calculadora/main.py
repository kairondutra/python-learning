
valores = {0: "primeiro", 1: "segundo"}
operacoes_validas = {"+", "-", "*", "/"}

# Função para realizar cálculos
def calcular(valor1, valor2, operacao):
    operacoes = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Erro: Não é possível dividir por zero."
    }
    return operacoes[operacao](valor1, valor2)

print("-".center(40, "-") + "\n" + "Calculadora".center(40) + "\n" + "-".center(40, "-"))

while True:
    lista = []
    
    while True:
        operacao = input("Escolha uma operação (+, -, *, /): ")
        if operacao in operacoes_validas:
            break
        print("⚠️ Operação inválida! Escolha entre +, -, *, /.")
    
    # Capturando os dois valores
    for i in range(len(valores)):
        while True:
            try:
                valor = input(f"Informe o {valores[i]} valor: ")
                lista.append(float(valor))
                break
            except ValueError:
                print("⚠️ Entrada inválida! Digite um número válido.")

    # Realizando o cálculo
    resultado = calcular(lista[0], lista[1], operacao)
    
    # Exibindo o resultado
    print(f"{lista[0]} {operacao} {lista[1]} = {resultado:.2f}" if isinstance(resultado, (int, float)) else resultado)
    print("-" * 40 + "\n")
    
    # Perguntar se deseja continuar
    continuar = input("Deseja fazer outro cálculo? (s/n): ").strip().lower()
    if continuar not in ("s", "sim"):
        break
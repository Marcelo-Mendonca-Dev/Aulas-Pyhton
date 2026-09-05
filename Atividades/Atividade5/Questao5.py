# Questão 5: Calculadora Básica de Dois Números.

# Pede os dois numeros (float pra poder usar quebrado com ponto).
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Pede pro usuario escolher qual conta quer fazer.
operador = input("Escolha a operação (+, -, *, /): ")

# O match/case vai olhar o simbolo digitado e ja calcular direto no print.
match operador:
    case "+":
        print("Resultado da soma:", num1 + num2)
    case "-":
        print("Resultado da subtração:", num1 - num2)
    case "*":
        print("Resultado da multiplicação:", num1 * num2)
    case "/":
        # Faz a divisao normal dos dois valores
        print("Resultado da divisão:", num1 / num2)
    case _:
        # Se digitou qualquer letra ou simbolo doido fora das quatro operacoes.
        print("Operação inválida!")
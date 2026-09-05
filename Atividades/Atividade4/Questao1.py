# Questão 1: O Verificador de Par ou Ímpar

# Pede pro usuario mandar um numero inteiro qualquer
numero = int(input("Digite um numero inteiro: "))

# Checar se o resto da divisao por 2 dá zero

if numero % 2 == 0:
    print("O numero", numero, "e PAR")
else:
    # Se sobrou resto, com certeza o numero e impar
    print("O numero", numero, "e IMPAR")
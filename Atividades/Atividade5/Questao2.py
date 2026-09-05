# Questão 2: Classificador de Vogais e Consoantes.

# Pede a letra e usa .lower() so pra garantir que funcione mesmo se digitarem maiuscula.
letra = input("Digite uma unica letra: ").lower()

# Estrutura match/case pra testar a letra digitada.
match letra:
    # Agrupa todas as vogais numa linha so usando o pipe | (que funciona tipo um OU).
    case "a" | "e" | "i" | "o" | "u":
        print("Você digitou uma vogal.")
    # O _ pega qualquer outra coisa que nao caiu no caso de cima.
    case _:
        print("Não é uma vogal.")
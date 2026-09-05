# Questão 3: Turno de Estudo.

# Pede pro aluno digitar a letra do turno dele.
turno = input("Em qual turno voce estuda? (M - Matutino, V - Vespertino, N - Noturno): ")

# O match/case vai conferir a letra que foi digitada.
match turno:
    # Agrupa a versao maiuscula e minuscula com o pipe | pra nao dar erro.
    case "M" | "m":
        print("Bom Dia!")
    case "V" | "v":
        print("Boa Tarde!")
    case "N" | "n":
        print("Boa Noite!")
    # O _ funciona como o 'else', pega qualquer letra ou simbolo fora do esperado.
    case _:
        print("Turno inválido!")
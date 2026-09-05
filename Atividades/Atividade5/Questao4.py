# Questão 4: Estações do Ano.

# Pede pro usuario o numero do mes (de 1 a 12).
mes = int(input("Digite o numero do mes (1 a 12): "))

# Usa o match/case pra checar em qual estacao o mês cai.
match mes:
    # Dezembro, Janeiro e Fevereiro (calorzao).
    case 12 | 1 | 2:
        print("Verão")
    # Marco, Abril e Maio.
    case 3 | 4 | 5:
        print("Outono")
    # Junho, Julho e Agosto (friozinho).
    case 6 | 7 | 8:
        print("Inverno")
    # Setembro, Outubro e Novembro.
    case 9 | 10 | 11:
        print("Primavera")
    # Caso digite 0, 13 ou qualquer outro numero fora do calendario.
    case _:
        print("Mês inválido!")
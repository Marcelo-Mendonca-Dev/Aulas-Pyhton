# Atividade 8 - Calculo de Media do Aluno.

# Funcao simples que recebe o nome e as quatro notas.
def resultado_aluno(nome, n1, n2, n3, n4):
    # Soma as 4 notas e divide por 4 pra achar a media.
    media = (n1 + n2 + n3 + n4) / 4

    # Mostra os dados do aluno na tela.
    print("Nome do aluno:", nome)
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Nota 3:", n3)
    print("Nota 4:", n4)
    print("Media final:", media)

    # Checar se passou ou se rodou.
    if media >= 7:
        print("Status: Aprovado")
    else:
        print("Status: Reprovado")


# Pegando os dados digitados pelo usuario.
nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

# Chamando a funcao pra rodar.
resultado_aluno(nome, n1, n2, n3, n4)
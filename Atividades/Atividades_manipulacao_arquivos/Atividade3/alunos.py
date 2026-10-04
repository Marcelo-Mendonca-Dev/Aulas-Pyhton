def acrescentar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    turma = input("Digite a turma: ").strip()

    try:
        n1 = float(input("Nota do 1º Bimestre: "))
        n2 = float(input("Nota do 2º Bimestre: "))
        n3 = float(input("Nota do 3º Bimestre: "))
        n4 = float(input("Nota do 4º Bimestre: "))
    except ValueError:
        print("Erro: As notas devem ser valores numéricos.")
        return

    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    try:
        with open("alunos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"\n{nome};{turma};{n1:.1f};{n2:.1f};{n3:.1f};{n4:.1f};{status}")
        print(f"Aluno {nome} adicionado com sucesso!")
    except FileNotFoundError:
        print("Erro: Arquivo 'alunos.txt' não encontrado.")


def calcular_media_aluno():
    nome_busca = input("Digite o nome do aluno para calcular a média: ").strip()
    encontrado = False

    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue

                partes = linha_limpa.split(";")
                if partes[0].lower() == nome_busca.lower():
                    n1 = float(partes[2])
                    n2 = float(partes[3])
                    n3 = float(partes[4])
                    n4 = float(partes[5])
                    media = (n1 + n2 + n3 + n4) / 4
                    print(f"A média de {partes[0]} é {media:.2f}")
                    encontrado = True
                    break

        if not encontrado:
            print(f"Aluno '{nome_busca}' não encontrado.")
    except FileNotFoundError:
        print("Erro: Arquivo 'alunos.txt' não encontrado.")


def consultar_status_aluno():
    nome_busca = input("Digite o nome do aluno para consultar status: ").strip()
    encontrado = False

    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue

                partes = linha_limpa.split(";")
                if partes[0].lower() == nome_busca.lower():
                    status = partes[-1]
                    print(f"O aluno {partes[0]} está {status}.")
                    encontrado = True
                    break

        if not encontrado:
            print(f"Aluno '{nome_busca}' não encontrado.")
    except FileNotFoundError:
        print("Erro: Arquivo 'alunos.txt' não encontrado.")


def mostrar_maior_media_turma():
    turma_busca = input("Digite a Turma (ex: 101): ").strip()
    maior_media = -1.0
    melhor_aluno = ""
    turma_encontrada = False

    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue

                partes = linha_limpa.split(";")
                if partes[1].strip() == turma_busca:
                    turma_encontrada = True
                    n1 = float(partes[2])
                    n2 = float(partes[3])
                    n3 = float(partes[4])
                    n4 = float(partes[5])
                    media = (n1 + n2 + n3 + n4) / 4

                    if media > maior_media:
                        maior_media = media
                        melhor_aluno = partes[0]

        if turma_encontrada and melhor_aluno != "":
            print(f"Maior média da turma {turma_busca}: {melhor_aluno} com média {maior_media:.2f}")
        else:
            print(f"Nenhum aluno encontrado para a turma '{turma_busca}'.")
    except FileNotFoundError:
        print("Erro: Arquivo 'alunos.txt' não encontrado.")


while True:
    print("\n========== GESTÃO ESCOLAR ==========")
    print("1. Acrescentar um aluno")
    print("2. Calcular média de um aluno")
    print("3. Consultar status de aprovação")
    print("4. Mostrar a maior média da turma")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ").strip()

    if opcao == "1":
        acrescentar_aluno()
    elif opcao == "2":
        calcular_media_aluno()
    elif opcao == "3":
        consultar_status_aluno()
    elif opcao == "4":
        mostrar_maior_media_turma()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
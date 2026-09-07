# Questão 4: Menu Interativo.

# Inicializa com 0 só pra conseguir começar o loop.
opcao = 0

# O while roda direto e só para quando a opção for exatamente 2.
while opcao != 2:
    print("--- MENU ---")
    print("1 - Mostrar saudação")
    print("2 - Sair do programa")

    opcao = int(input("Escolha uma opção: "))

    # 1. Se digitar 1, manda a saudação
    if opcao == 1:
        print("Olá, seja muito bem-vindo(a)!")

    # 2. Se digitar qualquer coisa fora 1 e 2, avisa que tá errado.
    elif opcao != 2:
        print("Opção inválida!")

# 3. Saindo do laço (ou seja, digitou 2), encerra com a mensagem final.
print("Programa encerrado.")
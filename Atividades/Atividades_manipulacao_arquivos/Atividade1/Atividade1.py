cliente = input("Digite seu nome para iniciar a compra: ")

carrinho = []
total = 0.0

while True:
    nome_produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")
    if nome_produto.lower() == "fim":
        break

    preco = float(input(f"Digite o preço de {nome_produto}: "))
    carrinho.append([nome_produto, preco])
    total += preco

print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Cliente: {cliente}\n")
    arquivo.write("Itens Comprados:\n")
    for item in carrinho:
        arquivo.write(f"- {item[0]}: R$ {item[1]:.2f}\n")
    arquivo.write(f"TOTAL: R$ {total:.2f}\n")

print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

posicao_total = conteudo.find("TOTAL: ")
if posicao_total != -1:
    inicio_valor = posicao_total + len("TOTAL: ")
    valor_cobrado = conteudo[inicio_valor:].strip()
    print(f"Compra processada com sucesso! Valor cobrado: {valor_cobrado}")
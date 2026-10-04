usuario = input("Digite seu nome para iniciar a compra: ")

produtos = []
total = 0.0

while True:
    nome_produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")
    if nome_produto.lower() == "fim":
        break

    preco = float(input(f"Digite o preço de {nome_produto}: "))
    produtos.append([nome_produto, preco])
    total += preco

print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Cliente: {usuario}\n")
    arquivo.write("Itens Comprados:\n")
    for item in produtos:
        arquivo.write(f"- {item[0]}: R$ {item[1]:.2f}\n")
    arquivo.write(f"TOTAL: R$ {total:.2f}\n")

print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

posicao_total = texto.find("TOTAL: ")
if posicao_total != -1:
    total_texto = texto[posicao_total + len("TOTAL: "):].strip()
    print(f"Compra processada com sucesso! Valor cobrado: {total_texto}")
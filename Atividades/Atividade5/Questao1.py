# Questão 1: Menu da Lanchonete.

# Pede o codigo do lanche pro cliente escolher.
codigo = int(input("Digite o codigo do item (1 a 4): "))

# Vai testando cada codigo de 1 a 4 com if/elif.
if codigo == 1:
    print("Produto: Cachorro-quente | Preço: R$ 10,00")
elif codigo == 2:
    print("Produto: Hambúrguer | Preço: R$ 15,00")
elif codigo == 3:
    print("Produto: Batata Frita | Preco: R$ 8,00")
elif codigo == 4:
    print("Produto: Refrigerante | Preco: R$ 5,00")
else:
    # Se digitou qualquer numero fora do cardapio, barra aqui.
    print("Código inválido")
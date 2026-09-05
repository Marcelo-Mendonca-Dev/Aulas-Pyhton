# Questão 8: A Calculadora de Lucro da Empresa

# Pega o nome do item (texto puro) e os valores em dinheiro usando float
nome_produto = input("Digite o nome do produto: ")
custo = float(input("Digite o preco de custo de fabrica: R$ "))
preco_venda = float(input("Digite o preco de venda na loja: R$ "))

# Faz a continha basica pra ver quanto sobrou no bolso
lucro = preco_venda - custo

# Regra do comerciante: considera bom negocio se lucrar mais de 20 conto
lucro_bom = lucro > 20.00

# Joga o resumo na tela com nome, valor do lucro e se bateu a meta (True/False)
print("Produto:", nome_produto)
print("Lucro obtido: R$", lucro)
print("O lucro foi bom (> R$ 20.00)?", lucro_bom)
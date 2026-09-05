#Menu da Lanchonete

print("1 - Cachorro quente | R$10,00")
print("2 - Hamburguer      | R$15,00")
print("3 - Batata Frita    | R$8,00")
print("4 - Refrigerante    | R$5,00")

codigo = int(input("Digite do item (1 a 4): "))

if codigo == 1:
    print("Produto: Cachorro-quente")
    print("Preço: R$ 10,00")

elif codigo == 2:
    print("Produto: Hamburguer")
    print("Preço: R$ 15,00")

elif codigo == 3:
    print("Produto: Batata Frita")
    print("Preço: R$ 8,00")

elif codigo == 4:
    print("Produto: Refrigerante")
    print("Preço: R$ 5,00")

else:
    print("Codigo inválido")
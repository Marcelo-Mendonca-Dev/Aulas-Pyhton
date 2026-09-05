# Questão 3: O Validador de Idade para Votação.

# Pede a idade da pessoa, numero inteiro normal.
idade = int(input("Digite a sua idade: "))

# Checa a regra da maioridade pra voto obrigatorio (18 anos pra cima).
if idade >= 18:
    print("Você é obrigado a votar")
else:
    # Se tiver menos de 18, nao tem essa obrigacão ainda.
    print("Você ainda não é obrigado a votar")
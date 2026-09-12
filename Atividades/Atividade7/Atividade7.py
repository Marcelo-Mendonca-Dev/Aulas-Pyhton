# Atividade 7 - Gerenciamento de Funcionarios

# Lista vazia pra guardar todos os funcionarios cadastrados.
funcionarios = []

# Variavel de controle pro while continuar rodando.
continuar = "s"

# While pra cadastrar quantos funcionarios o usuario quiser.
while continuar == "s" or continuar == "S":
    nome = input("Digite o nome do funcionario: ")
    # Adiciona o nome no final da lista
    funcionarios.append(nome)

    # Pergunta se quer continuar cadastrando.
    continuar = input("Deseja cadastrar outro funcionario? (s/n): ")

# Duas listas vazias pra separar a galera
aumento = []
demitidos = []

# Usa o for com range e len pra percorrer os indices (0, 1, 2, 3...)
for i in range(len(funcionarios)):
    # Regra pelo index: se o index for par, ganha aumento.
    # Se o index for impar, entra na lista de demissao.
    if i % 2 == 0:
        aumento.append(funcionarios[i])
    else:
        demitidos.append(funcionarios[i])

# Mostra o resultado final das duas listas.
print("\n--- Funcionarios que receberao aumento (indice par) ---")
for f in aumento:
    print(f)

print("\n--- Funcionarios que serao demitidos (indice impar) ---")
for f in demitidos:
    print(f)
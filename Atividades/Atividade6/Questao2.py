# Questão 2: Validação de Senha.

# Senha correta ja definida direto no codigo como texto.
senha_correta = "123456"

# Primeira tentativa: pede pro usuario digitar a senha.
senha_digitada = input("Digite a senha: ")

# Enquanto o que foi digitado for diferente (!=) da senha certa, fica preso aqui.
while senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
    # Pede de novo aqui dentro pro loop nao ficar infinito.
    senha_digitada = input("Digite a senha: ")

# So chega nessa linha quando o usuario finalmente acertar a senha.
print("Acesso permitido!")
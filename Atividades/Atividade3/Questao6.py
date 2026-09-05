# Questão 6: O Erro de Verificação (Análise e Correção de Código)

# EXPLICAÇÃO DO ERRO:
# O input() sempre devolve o que o usuario digita no formato texto (string/str).
# A variavel original guardava 1234 como numero (int).
# Pro Python, o numero 1234 e o texto "1234" sao coisas diferentes,
# por isso a comparacao sempre dava False, mesmo digitando certo.

# CORREÇÃO:
# Guardamos a senha cadastrada direto como texto (entre aspas)
senha_cadastrada = "1234"

# Agora o input() ler o texto digitado normalmente sem dar choque de tipos
senha_digitada = input("Digite sua senha: ")

# Aqui compara string com string ("1234" == "1234"), dando True certinho
acesso_liberado = senha_cadastrada == senha_digitada

# Mostra o status de acesso na tela
print("Acesso liberado?", acesso_liberado)
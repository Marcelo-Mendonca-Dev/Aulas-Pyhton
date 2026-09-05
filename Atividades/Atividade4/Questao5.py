# Questão 5: A Catraca VIP de Eventos (Uso de AND e OR no if).

# Pede os dados do convidado na portaria (1 pra sim e 0 pra nao).
idade = int(input("Digite sua idade: "))
tem_vip = int(input("Possui convite VIP? (1 para Sim, 0 para Não): "))
eh_organizador = int(input("É organizador do evento? (1 para Sim, 0 para Não): "))

# Regra da catraca:
# Precisa ser maior de idade E ter VIP (colocamos entre parenteses pra amarrar essa dupla).
# OU ser da organizacao (ai passa direto, nao importa a idade).
if (idade >= 18 and tem_vip == 1) or eh_organizador == 1:
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:
    # Se nao se encaixar em nenhuma das opcoes, barra a entrada.
    print("Entrada NEGADA! Você não atende aos requisitos")
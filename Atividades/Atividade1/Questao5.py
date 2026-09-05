# questao 5 - calculo de idade

#Pegando os anos digitados e convertendo direto pra numero inteiro
ano_nasc = int(input("Digite o ano que você nasceu: "))
ano_atual = int(input("Digite o ano atual: "))

#Calculando a idade pela diferença dos anos
idade = ano_atual - ano_nasc

#Mostrando a idade na tela
print("Você tem (ou vai fazer)", idade, "anos!")
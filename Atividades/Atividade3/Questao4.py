# Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)

# Entrada dos dados: notas com virgula/ponto e a presenca do aluno.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
freq = float(input("Digite a frequencia do aluno: "))

# Tira a media basica somando tudo e dividindo por 2 (tem que usar parenteses pra somar primeiro)
media = (nota1 + nota2) / 2

# Checa as duas coisas de uma vez com o 'and': so da True se a media for 6+ E a frequencia 75%+
aprovado = media >= 6.0 and freq >= 75

# Joga o resultado final na tela pra ver a media e se o aluno passou ou rodou
print("Media:", media)
print("Aprovado:", aprovado)
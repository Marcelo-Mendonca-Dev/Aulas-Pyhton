#Questao 2 - média do semestre

#Pegando os dados do aluno errado

nome = input("Digite seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

#Calculo da media (com parenteses pra somar antes de dividir)
media = (n1 + n2 + n3) / 3

# Exibindo a media final
print("Olá", nome, ", a sua média final de", round(media, 2))

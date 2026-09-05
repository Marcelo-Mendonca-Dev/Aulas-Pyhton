# Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições)

# Pede a idade (numero inteiro) e o peso (com float pra aceitar gramas, tipo 52.5)
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso em kg: "))

# Checar todas as regras juntas usando o 'and':
# Precisa ter de 16 pra cima, ate 69 anos E pesar estritamente mais que 50kg
pode_doar = idade >= 16 and idade <= 69 and peso > 50

# Mostra na tela se a pessoa ta liberada pra doacao (True) ou nao (False)
print("Pode doar sangue?", pode_doar)
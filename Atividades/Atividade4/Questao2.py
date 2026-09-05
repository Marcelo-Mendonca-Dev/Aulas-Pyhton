# Questão 2: O Radar de Velocidade

# Pede a velocidade do carro (float pq o velocimetro pode marcar quebrado tipo 82.5)
velocidade = float(input("Digite a velocidade atual do carro em km/h: "))

# Checa se passou do limite da pista que eh 80 km/h
if velocidade > 80:
    # Se passou de 80, ja era, tomou multa
    print("Você foi multado por excesso de velocidade!")
else:
    # Se tiver em 80 certinho ou menos, ta liberado
    print("Velocidade dentro do limite permitido. Boa viagem!")
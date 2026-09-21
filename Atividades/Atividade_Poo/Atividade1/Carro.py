class Carro:
    def __init__(self, dono, cor, tipo, modelo, ano, fabricante):
        self.__dono = dono
        self.cor = cor
        self.tipo = tipo
        self.__modelo = modelo
        self.ano = ano
        self.fabricante = fabricante

    def __str__(self):
        return (f"Informações do carro:"
                f"\n\tDono: {self.__dono}"
                f"\n\tCor: {self.cor}"
                f"\n\tTipo: {self.tipo}"
                f"\n\tModelo: {self.__modelo}"
                f"\n\tAno: {self.ano}"
                f"\n\tFabricante: {self.fabricante}")

    def buzinar(self):
        print("O carro buzinou")

    def acelerar(self):
        print(f"O {self.__dono} acelerou o {self.__modelo}")

    def bater(self):
        self.__modelo = "Sucata"


carro_Gustavo = Carro(
    "Gustavo",
    "Vermelho",
    "Popular",
    "Fiesta",
    2016,
    "Ford")

carro_Vinicius = Carro(
    "Vinicius",
    "Amarelo",
    "Esportivo",
    "Camaro",
    2025,
    "GM")

carro_Victor = Carro(
    "Victor",
    "Azul",
    "Eletrico",
    "BYD",
    2025,
    "BYD")

carro_Marcelo = Carro(
    "Marcelo",
    "Preto",
    "Popular",
    "Gol",
    2018,
    "VW")

carro_Adele = Carro(
    "Adele",
    "Branco",
    "Sedan",
    "Civic",
    2022,
    "Honda")

lista_carros = [carro_Gustavo, carro_Vinicius, carro_Victor, carro_Marcelo, carro_Adele]

for carro in lista_carros:
    print(carro)
    print("Mostras 5 Listas Carros")
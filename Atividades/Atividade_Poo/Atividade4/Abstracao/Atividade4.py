
from abc import ABC, abstractmethod



class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):

        pass

    def amortizar(self, parcela, metodo):
        print(f"Amortizando a {parcela}º parcela via {metodo}.")


class Pix(Pagamento):
    def pagar(self, valor):
        print("Desconto de 10% no PIX")
        desconto = valor * 0.10
        print(f"Pagando R${(valor - desconto):.2f} via PIX")



class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor} via BOLETO")


class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor} no debido via CARTAO")

    def parcelar(self, valor):
        print(f"Pagando R${valor} parcelado via CARTAO")


class Principal:

    def efetuar_pagamento(metodo_pagamento: Pagamento, valor: float):
        print(f"Efetuando pagamento...")
        metodo_pagamento.pagar(valor)
        print("Pagamento efetuado com sucesso!\n")

    print("====== EFETUANDO PAGAMENTOS ======")
    lista_pagamentos = [
        (Pix(), 250),
        (Cartao(), 100.00),
        (Boleto(), 5000.00)
    ]


    for metodo_pagamento, valor in lista_pagamentos:
        efetuar_pagamento(metodo_pagamento, valor)
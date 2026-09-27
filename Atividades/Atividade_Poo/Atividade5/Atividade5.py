class ItemPedido:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        try:
            self.valor = float(valor)
        except ValueError:
            raise ValueError(f"Erro: O valor para '{self.descricao}' deve ser estritamente numérico.")


class Mesa:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.pedidos = []

    def adicionar_pedido(self, item):
        self.pedidos.append(item)
        print(f"-> {item.descricao} adicionado à {self.numero_mesa}.")

    def somar_total(self):
        total = 0.0
        for item in self.pedidos:
            total += item.valor
        return total

    def fechar_conta(self, taxa_servico):
        subtotal = self.somar_total()
        valor_taxa = subtotal * (taxa_servico / 100)
        total_final = subtotal + valor_taxa

        print(f"Extrato da {self.numero_mesa}:")
        if not self.pedidos:
            print("  Nenhum pedido registrado.")
        else:
            for item in self.pedidos:
                print(f"  - {item.descricao}: R$ {item.valor:.2f}")

        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Taxa de Serviço ({taxa_servico}%): R$ {valor_taxa:.2f}")
        print(f"Total a pagar: R$ {total_final:.2f}")

        self.pedidos.clear()


def registrar_pedido_seguro(mesa, descricao, valor):
    try:
        item = ItemPedido(descricao, valor)
        mesa.adicionar_pedido(item)
    except ValueError as erro:
        print(f"Alerta do sistema: {erro}")


mesa1 = Mesa("Mesa 1")

registrar_pedido_seguro(mesa1, "Pizza Margherita", 45.90)
registrar_pedido_seguro(mesa1, "Refrigerante", 8.50)

print("\n--- Testando entrada invalida ---")
registrar_pedido_seguro(mesa1, "Pudim", "quinze")
registrar_pedido_seguro(mesa1, "Café", "5,50")

registrar_pedido_seguro(mesa1, "Suco de Laranja", 12.00)

print("\n--- Fechamento da conta ---")
mesa1.fechar_conta(taxa_servico=10)

print("\n--- Verificando status da mesa após fechamento ---")
mesa1.fechar_conta(taxa_servico=10)
class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, novo_quantidade_estoque):
        self.__quantidade_estoque = novo_quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if 0 < quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
        else:
            print("Venda negada: Estoque insuficiente")

    def aplicar_desconto(self, percentual):
        if 0 < percentual <= 80:
            self.__preco = self.__preco - (self.__preco * (percentual / 100))
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Estoque: {self.__quantidade_estoque}")



meu_produto = Produto("Notebook", 3500.00, 10)


meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100


meu_produto.realizar_venda(9999)


meu_produto.exibir_resumo()


print(meu_produto.__dict__)
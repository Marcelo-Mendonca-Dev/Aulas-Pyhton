from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento

# ==========================================
# COMBUSTÍVEIS
# ==========================================
etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

# ==========================================
# VEÍCULOS
# ==========================================
carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")
limosine = Veiculo("Limosine", "ABC-0001")
onibus = Veiculo("Onibus", "ABC-0002")

# ==========================================
# ABASTECIMENTOS
# ==========================================
abastecimento1 = Abastecimento(carro, etanol, 50)
abastecimento2 = Abastecimento(moto, gasolina, 25)
abastecimento3 = Abastecimento(van, diesel, 200)
abastecimento4 = Abastecimento(limosine, gasolina, 400)
abastecimento5 = Abastecimento(onibus, diesel, 600)
abastecimento6 = Abastecimento(carro, gasolina, 150)

# ==========================================
# LISTA DE ABASTECIMENTOS ATUALIZADA
# ==========================================
abastecimentos = [abastecimento1, abastecimento2,
                  abastecimento3, abastecimento4,
                  abastecimento5, abastecimento6]

# ==========================================
# MOSTRANDO OS ABASTECIMENTOS
# ==========================================
print("========== ABASTECIMENTOS DO DIA ==========")
for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()

# ==========================================
# TOTAL DE VENDAS POR COMBUSTÍVEL
# ==========================================
total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:
    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor
    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor
    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor

# ==========================================
# TOTAL DO DIA
# ==========================================
total_dia = (total_etanol + total_gasolina + total_diesel)

with open("recibo_posto.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("========== POSTO DE GASOLINA ==========")
    for abs in abastecimentos:
        arquivo.write(f"\n{abs.veiculo}"
                      f"\nCombustível: {abs.combustivel.nome}\n"
                      f"Valor: R${abs.valor}\n")
    arquivo.write("\n========================================\n")
    arquivo.write(f"Etanol: {total_etanol}\n"
                  f"Gasolina: {total_gasolina}\n"
                  f"Diesel: {total_diesel}\n"
                  f"TOTAL DO DIA: {total_dia}")

with open("recibo_posto.txt", 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

    posicao_etanol = texto.find("Etanol:")
    etanol_texto = texto[posicao_etanol + len("Etanol: "): posicao_etanol + 10]

    posicao_gasolina = texto.find("Gasolina:")
    gasolina_texto = texto[posicao_gasolina + len("Gasolina: "): posicao_gasolina + 13]

    posicao_diesel = texto.find("Diesel:")
    diesel_texto = texto[posicao_diesel + len("Diesel: "): posicao_diesel + 11]

    posicao_total_dia = texto.find("TOTAL DO DIA: ")
    total_dia_texto = texto[posicao_total_dia+len("TOTAL DO DIA: "): posicao_total_dia+18]

    print(f"\nTotal ganho ETANOL: {etanol_texto}"
          f"\nTotal ganho GASOLINA: {gasolina_texto}"
          f"\nTotal ganho Diesel: {diesel_texto}"
          f"\nTOTAL DO DIA: {total_dia_texto}")
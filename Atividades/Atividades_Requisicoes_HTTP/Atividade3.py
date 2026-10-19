import json
import requests

url_base = "http://192.168.205.100:8080/funcionarios"


with open("dados_funcionarios_atualizados.json", "r", encoding="utf-8") as arquivo:
    lista_funcionarios = json.load(arquivo)


for funcionario in lista_funcionarios:
    id_funcionario = funcionario["id"]
    url_put = f"{url_base}/{id_funcionario}"

    dados_atualizados = {
        "id": funcionario["id"],
        "nome": funcionario["nome"],
        "cargo": funcionario["cargo"],
        "salario": funcionario["salario"],
        "tempoEmpresa": funcionario["tempoEmpresa"],
        "cep": funcionario["cep"],
        "cidade": funcionario["cidade"],
        "estado": funcionario["estado"]
    }

    resposta_put = requests.put(url_put, json=dados_atualizados)


    if resposta_put.status_code == 200:
        print(f"Funcionário {id_funcionario} ({funcionario['nome']}) atualizado com sucesso! Status: 200")
    else:
        print(f"Erro ao atualizar funcionário {id_funcionario}. Status: {resposta_put.status_code}")


print("\n--- LISTAGEM FINAL DE FUNCIONÁRIOS NA API ---")
busca = requests.get(url_base)
if busca.status_code == 200:
    for f in busca.json():
        print(f)
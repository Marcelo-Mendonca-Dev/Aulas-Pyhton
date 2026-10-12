import json
import requests


try:
    with open("historico_pesquisa.json", "r", encoding="utf-8") as arquivo:
        dicinario_dados_cep = json.load(arquivo)
        if not isinstance(dicinario_dados_cep, list):
            dicinario_dados_cep = []
except (FileNotFoundError, json.JSONDecodeError):
    dicinario_dados_cep = []


while True:
    cep_digitado = input("Digite o CEP: ").strip().replace("-", "")
    link = f"https://viacep.com.br/ws/{cep_digitado}/json/"


    try:
        resposta = requests.get(link, timeout=5)
        resposta.raise_for_status()
        dados_api = resposta.json()
    except requests.exceptions.RequestException:
        print("Erro: Falha na conexão com o serviço ViaCEP.")
        opcao = input("\nDigite 'sair' para finalizar ou Enter para tentar outro CEP: ").strip().lower()
        if opcao == "sair":
            break
        continue


    if "erro" in dados_api:
        print("Erro: CEP não encontrado na base de dados.")
    else:
        # Exibição dos dados retornados
        print(f"\nLogradouro: {dados_api.get('logradouro', '')}")
        print(f"Bairro: {dados_api.get('bairro', '')}")
        print(f"Cidade: {dados_api.get('localidade', '')}")
        print(f"Estado: {dados_api.get('uf', '')}\n")


        novo_registro = {
            "cep": dados_api.get("cep", cep_digitado),
            "logradouro": dados_api.get("logradouro", ""),
            "bairro": dados_api.get("bairro", ""),
            "cidade": dados_api.get("localidade", ""),
            "estado": dados_api.get("uf", "")
        }


        dicinario_dados_cep.append(novo_registro)

     
        with open("historico_pesquisa.json", "w", encoding="utf-8") as arquivo:
            json.dump(dicinario_dados_cep, arquivo, ensure_ascii=False, indent=4)

        print("Pesquisa registrada no histórico com sucesso!")

    opcao = input("\nDigite 'sair' para finalizar ou Enter para nova consulta: ").strip().lower()
    if opcao == "sair":
        break
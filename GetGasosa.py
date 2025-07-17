import requests
from AuthGasosa import get_auth
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()
cpf = os.getenv("cpf")
pw = os.getenv("pw")


class GasPriceApiClient:
    BASE_URL = "https://api.set.rn.gov.br/nfp/v1/preco-minimo"
    CLIENT_ID = "62cccea10501"

    def __init__(self, cpf, password):
        self.cpf = cpf
        self.password = password
        self.session = requests.session()

    def _get_auth_token(self):
        return get_auth(self.cpf, self.password)

    def search_product(self, city, product_gtin):
        token = self._get_auth_token()
        headers = {
            "client_id": self.CLIENT_ID,
            "Authorization": f"Bearer {token}",
            "cpf": self.cpf,
        }
        params = {"gtins": product_gtin, "municipios": city}
        response = self.session.get(
            f"{self.BASE_URL}/pesquisar-produto", params=params, headers=headers
        )
        response.raise_for_status()  # Lança exceção para respostas com erro (4xx ou 5xx)
        return response.json()


def GetGasosa(cidade, produto):
    
    api_client = GasPriceApiClient(cpf, pw)
    
    try:
        payload = api_client.search_product(cidade, produto)
        filtered_results = []
        for item in payload.get("result", {}).get("value", []):
            if item.get("nomeFantasia"):  # Checa se a chave existe e não é vazia
                filtered_results.append(item)
        return filtered_results
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição à API: {e}")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return []

def GetDetails(cidade, produto):
    payload = GetGasosa(cidade, produto)
    notas = []
    if not payload:
        print("Nenhum resultado encontrado para processar.")
        return notas

    for item in payload:
        nota = {
            "dataEmissao": item.get("dataEmissao", ""),
            "nomeFantasia": item.get("nomeFantasia", ""),
            "municipio": item.get("municipio", ""),
            "bairro": item.get("bairro", ""),
            "logradouro": item.get("logradouro", ""),
            "produto": item.get("produto", ""),
            "valorUnitarioComercial": item.get("valorUnitarioComercial", ""),
            "idade": item.get("idade", ""),
            "mapsLogradouro": item.get("mapsLogradouro", ""),
            "mapsBairro": item.get("mapsBairro", ""),
            "mapsCidade": item.get("mapsCidade", ""),
            "principioAtivo": item.get("principioAtivo", ""),
            "valorDesconto": item.get("valorDesconto", ""),
            "valorFinal": item.get("valorFinal", ""),
        }
        notas.append(nota)

    for i, nota in enumerate(notas):
        print(f"--- Detalhes da Nota {i + 1} ---")
        for property, value in nota.items():
            print(f"{property}: {value}")
    return notas

import requests

def get_auth(cpf,pw):
    s = requests.Session()
    cooks ={
    "_ga_R5521T1KDN": "GS1.1.1722546704.2.0.1722546704.0.0.0",
    "_gid": "GA1.4.2144048125.1722860439",
    "_ga_00KWX5GWM5": "GS1.1.1722860439.10.1.1722863842.0.0.0",
    "_ga": "GA1.1.1332807888.1720630342",
    "SET-AUTH-RS" : "E82qnMDSNzwq%2fJ2QcJsSvcVDGrDH9cyt3gdjTNVV6J7Z5rJQz%2f9eTBQQ%2bzqknRQnv%2faDIyK4jAOu6vuSXHrQkA%3d%3d, SET-AUTH-EK = ZTQ0NGRkNTg1ZQ%3d%3d%3aUkTNZA4ci0ttk7bFNyXagg%3d%3d",
    }
    response = s.get("https://api.set.rn.gov.br/autnpbasic/v1/notafiscalpotiguar/signin/basic",
        params={
                "client_id": "62cccea10501",
                "redirect_uri": "https:%2F%2Fuvt.set.rn.gov.br",
                "response_type": "code+id_token",
                "scope": "openid",
                "state": "kvxti8xnd4",
        },
        auth=(cpf,pw),
        headers={
            "client_id": "62cccea10501",
            "cpf": cpf,
            "priority": "u=1, i",},)
    payload = response.json()
    return payload["result"]["token"]["id_token"]




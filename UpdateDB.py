from GetGasosa import GetGasosa
import sqlalchemy as db

engine = db.create_engine("sqlite:///db.sql")
connection = engine.connect()
metadata = db.MetaData()


def update_db(cidade, produto):
    notas = GetGasosa(cidade, produto)
    if not notas:
        print("Nenhum resultado encontrado para atualizar o banco de dados.")
        return

    notas_table = db.Table("notas", metadata, autoload_with=engine)

    for nota in notas:
        query = db.insert(notas_table).values(
            dataEmissao=nota.get("dataEmissao", ""),
            nomeFantasia=nota.get("nomeFantasia", ""),
            municipio=nota.get("municipio", ""),
            bairro=nota.get("bairro", ""),
            logradouro=nota.get("logradouro", ""),
            produto=nota.get("produto", ""),
            valorUnitarioComercial=nota.get("valorUnitarioComercial", ""),
            idade=nota.get("idade", ""),
        )
        connection.execute(query)

    print(f"{len(notas)} registros atualizados no banco de dados.")

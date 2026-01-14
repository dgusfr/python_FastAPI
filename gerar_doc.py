import json
import os
from main import app


pasta = "docs"
arquivo = "openapi.json"
caminho_completo = os.path.join(pasta, arquivo)


if not os.path.exists(pasta):
    os.makedirs(pasta)


schema = app.openapi()


with open(caminho_completo, "w") as f:
    json.dump(schema, f)

print("Arquivo gerado com sucesso em: " + caminho_completo)

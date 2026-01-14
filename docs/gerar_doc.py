import json
from main import app

schema = app.openapi()

with open("openapi.json", "w") as f:
    json.dump(schema, f)

print("Arquivo openapi.json gerado com sucesso!")

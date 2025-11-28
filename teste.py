"""Desenvolva um programa Python para acessar, processar e organizar dados de cardápios de restaurantes de uma fonte externa. Inicialmente, o script deve utilizar a biblioteca requests para realizar uma requisição GET à URL https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json.

Após a requisição, caso ela seja bem sucedida, o conteúdo deve ser deserializado para um objeto JSON, crie um dicionário para agrupar os itens do cardápio com base na chave "Company", que representa o nome do restaurante.

Para cada restaurante, o valor associado no dicionário deve ser uma lista contendo os detalhes do item: "Item", "price" e "description". O segundo passo e objetivo final é a persistencia dos dados organizados. O script deve iterar sobre este dicionário recém-criado e, para cada restaurante, salvar sua lista de itens em um arquivo JSON individual, utilizando a biblioteca json.

O nome de cada arquivo deve seguir o padrão {Nome do Restaurante}, e o conteúdo salvo deve estar formatado com uma indentação de 4 espaços para melhor legibilidade. Por fim, o programa deve imprimir o dicionário Python completo contendo todos os restaurantes e seus respectivos cardápios agrupados, confirmando a correta organização dos dados antes da gravação nos arquivos.
"""

import requests

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json](https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}

    for restaurante in dados_json:
        nome_restaurante = restaurante["Company"]

    dados_restaurante[nome_restaurante].append(
        {
            "item": restaurante["Item"],
            "price": restaurante["price"],
            "description": restaurante["description"],
        }
    )

"""Desenvolva um programa Python para acessar, processar e organizar dados de cardápios de restaurantes. Inicialmente, o script deve utilizar a biblioteca requests para realizar uma requisição GET à URL https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json.

Após a requisição, caso ela seja bem sucedida, o conteúdo deve ser deserializado para um objeto JSON, crie um dicionário para agrupar os itens do cardápio com base na chave "Company", que representa o nome do restaurante.

Para cada restaurante, o valor associado no dicionário deve ser uma lista contendo os detalhes do item: "Item", "price" e "description". O segundo passo e objetivo final é a persistencia dos dados organizados. O script deve iterar sobre este dicionário recém-criado e, para cada restaurante, salvar sua lista de itens em um arquivo JSON individual, utilizando a biblioteca json.

O nome de cada arquivo deve seguir o padrão {Nome do Restaurante}, e o conteúdo salvo deve estar formatado com uma indentação de 4 espaços para melhor legibilidade. Por fim, o programa deve imprimir o dicionário Python completo contendo todos os restaurantes e seus respectivos cardápios agrupados, confirmando a correta organização dos dados antes da gravação nos arquivos.
"""

import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()
    data_restaurant = {}

    for restaurant in data_json:
        name_restaurant = restaurant["Company"]
        if name_restaurant not in data_restaurant:
            data_restaurant[name_restaurant] = []

        data_restaurant[name_restaurant].append(
            {
                "item": restaurant["Item"],
                "price": restaurant["price"],
                "description": restaurant["description"],
            }
        )

else:
    print(f"Error: {response.status_code}")

for restaurant_name, items in data_restaurant.items():
    file_name = f" {restaurant_name}.json"
    with open(file_name, "w") as file_restaurants:
        json.dump(items, file_restaurants, indent=4)


print(data_restaurant)

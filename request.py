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

from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get("/api/restaurants/")
def get_restaurants(restaurant: str = Query(None)):
    """
    Fetches restaurant data from an external API and returns the menu for a specific restaurant
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    response = requests.get(url)

    if response.status_code == 200:
        data_json = response.json()
        if restaurant is None:
            return {"Dados": data_json}

        data_restaurant = []
        for restaurant in data_json:
            if restaurant["Company"] == restaurant:
                data_restaurant.append(
                    {
                        "item": restaurant["Item"],
                        "price": restaurant["price"],
                        "description": restaurant["description"],
                    }
                )
        return {"Restaurant": restaurant, "Menu": data_restaurant}

    else:
        print(f"Error: {response.status_code} - {response.text}")

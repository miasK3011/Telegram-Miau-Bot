import requests

def getCatImage():
    api_url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(api_url)
    cat_url = None

    if response.status_code == 200:
        cat_data = response.json()
        cat_url = cat_data[0]["url"]
        #print(f"A URL da imagem do gato é: {cat_url}")
        
    return cat_url
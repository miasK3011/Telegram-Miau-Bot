import requests

def getDogImage():
    api_url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(api_url)
    dog_url = None

    if response.status_code == 200:
        dog_data = response.json()
        dog_url = dog_data["message"]
    if response.status_code == 400:
        dog_url = None

    return dog_url
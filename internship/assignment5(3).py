import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        print("Joke:", joke["setup"])
        print(" punchline:", joke["punchline"])
    else:
        print("Failed to fetch joke")

get_joke()
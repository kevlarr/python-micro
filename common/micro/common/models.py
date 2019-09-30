import requests

class RandomQuote:
    message: str

    def __init__(self):
        self.message = requests.get("https://api.kanye.rest", timeout=5).json()["quote"]

import requests

class RandomQuote:
    quote: str

    def __init__(self):
        self.quote = requests.get("https://api.kanye.rest", timeout=5).json()["quote"]

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os


def scrape_price(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-GB,en;q=0.9"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise Exception("Nepavyko pasiekti puslapio")

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")
    price = soup.find("p", class_="price_color")

    if not title or not price:
        raise Exception("Nepavyko rasti kainos arba pavadinimo")

    return {
        "title": title.text.strip(),
        "price": price.text.strip(),
        "url": url,
        "date": datetime.now().isoformat()
    }


def save_price_history(data, filename="data.json"):
    history = []

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            history = json.load(f)

    history.append(data)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

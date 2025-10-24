import requests
from bs4 import BeautifulSoup
import random


def meme_parsing():
    url = "https://www.anekdot.ru/random/mem/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
        "Referer": "https://www.anekdot.ru/"
    }

    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")


    images = []
    for img in soup.select("div.topicbox img"):
        src = img.get("src")
        if src and src.startswith("http") and src.endswith(".jpg"):
            images.append(src)

    if not images:
        return "😔 Не удалось найти мемы сейчас, попробуй позже!"

    return random.choice(images)











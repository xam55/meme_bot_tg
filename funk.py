import requests
from bs4 import BeautifulSoup
import random

HEADERS_COMMON = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/126.0.0.0 Safari/537.36"),
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
}

def meme_parsing():
    url = "https://www.anekdot.ru/random/mem/"
    headers = dict(HEADERS_COMMON, Referer="https://www.anekdot.ru/")

    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    images = []
    for img in soup.select("div.topicbox img"):
        src = img.get("src")
        if not src:
            src = img.get("data-src")
        if src and src.startswith("http") and (src.endswith(".jpg") or src.endswith(".jpeg") or src.endswith(".png")):
            images.append(src)

    if not images:
        return None

    return random.choice(images)


def it_meme_parsing():
    url = "https://pikabu.ru/tag/it%20юмор"
    headers = dict(HEADERS_COMMON, Referer="https://pikabu.ru/")

    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    images = []

    for img in soup.select("img.story-image__image"):
        src = img.get("data-src") or img.get("src")
        if src and src.startswith("http") and (src.endswith(".jpg") or src.endswith(".jpeg") or src.endswith(".png")):
            images.append(src)


    if not images:
        for img in soup.find_all("img"):
            src = img.get("data-src") or img.get("src")
            if src and "pikabu" in src and (src.endswith(".jpg") or src.endswith(".jpeg") or src.endswith(".png")):
                images.append(src)

    if not images:
        return None

    return random.choice(images)












import requests
from bs4 import BeautifulSoup


def get_soup(url: str, **params) -> BeautifulSoup | int:
    response = requests.get(url, **params)
    if response.status_code != 200:
        return response.status_code
    return BeautifulSoup(response.text, "html.parser")

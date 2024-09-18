from dataclasses import dataclass
from urllib.parse import urljoin

from utils.parser import get_soup


@dataclass
class News:
    link: str
    title: str
    preview_link: str | None = None


def parse_news(url: str) -> list[News]:
    soup = get_soup(url)
    news = []
    news_block = soup.find(class_="main-news__left")
    top = news_block.select(".main-news__left-hero")[0].find("a")
    news.append(News(
        urljoin(url, top["href"]),
        top.find(class_="main-news__left-hero-title").text
    ))
    other_news = soup.select("div.small-cards__default-item")
    for new in other_news:
        news.append(News(
            urljoin(url, new.div.a["href"]),
            new.a.text,
            new.find(class_='small-cards__default-img').img['src']
        ))
    return news

import requests
from bs4 import BeautifulSoup

def fetch_rss_feed(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="xml")
    items = soup.findAll("item")
    return [{
        "title": item.title.text,
        "pubDate": item.pubDate.text if item.pubDate else None,
        "description": item.description.text if item.description else None,
        "link": item.link.text
    } for item in items]

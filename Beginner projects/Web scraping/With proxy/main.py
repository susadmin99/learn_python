import requests
from bs4 import BeautifulSoup
import statistics

username, password = open('creds.txt').read().splitlines()

BASE_URL = "https://books.toscrape.com/"
url = BASE_URL + "catalogue/category/books/philosophy_7/index.html"

def proxy_request(url):
    payload = {
        "source": "Universal",
        "Url": url,
        "geo_location": "Germany"
    }

    response = requests.request(
        "POST", "https://realtime.oxylabs.io/v1/queries",
        auth = (username, password),
        json = payload
    )

    response_html = response.json()['results'][0]['content']
    return BeautifulSoup(response_html)


soup = proxy_request(url)

price_tags = soup.find_all("p", {"class": "price_color"})
prices = [float(price.text[1:]) for price in price_tags]

print(prices)
print(statistics.mean(prices))
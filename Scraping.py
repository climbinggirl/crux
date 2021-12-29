#learning basics of web scraping
import requests
from bs4 import BeautifulSoup

url = "https://efisco.net/category/jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="wp-polyfill-js-after")

print(results.prettify())
import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    random_article = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(random_article.content, 'html.parser')
    article_title = soup.find(id="firstHeading").text
    print(article_title, "\n Do you want to read this article? (Y/N)")
    answer = str(input(">"))

    if answer.lower() == "y":
        read_url = 'https://en.wikipedia.org/wiki/%s' %article_title
        webbrowser.open(read_url)
        break
    elif answer.lower() == "n":
        print("\n Let's try a different article")
        continue
    else:
        print("Wrong Input. Please write Y or N")
        break

import requests as r
import json

query = input("What type of news u want to see? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-08-18&sortBy=publishedAt&apiKey=c60bd4a2b8084f0f81db1e7d1510befc"
response = r.get(url)
# print(response.text)
news = json.loads(response.text)
# print(news,type(news))
for articles in news["articles"]:
    print(f"Title: {articles['title']}\nLink: {articles['url']}\nPublished At: {articles['publishedAt']}\n\n")

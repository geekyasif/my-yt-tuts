# pip install pywin32
# pip install request
# api_key : - https://newsapi.org/v2/top-headlines?source=bbc_news&country=us&apiKey=f44fe3073fa348b488d0c8ba983d8ef9

import requests
import json
from win32com.client import Dispatch

def speak_new(article):
    speak = Dispatch("SAPI.SpVoice")
    for i in range(len(article)):
        article = (i + 1, article[i])
        print("speak... :", article)
        speak.Speak(article)

if __name__ == '__main__':
    news = requests.get("https://newsapi.org/v2/top-headlines?source=bbc_news&country=us&apiKey=f44fe3073fa348b488d0c8ba983d8ef9")
    json_news = news.json()

    articles = json_news["articles"]
    articles_list = []

    for article in articles:
        articles_list.append(article["title"])

    speak_new(articles_list)
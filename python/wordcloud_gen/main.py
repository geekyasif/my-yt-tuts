import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import wikipedia

# creating a function to get data from wikipedia
def wiki(query):
    title = wikipedia.search(query[0])
    page = wikipedia.page(title)
    return page.content


# creating a fucntion to generate word cloud
def create_wordcloud(text):
    stopwords = STOPWORDS

    wc = WordCloud(
        background_color= 'black',
        stopwords = stopwords,
        height=500,
        width=400,
        max_words=40
    )

    wc.generate(text)
    wc.to_file('wordcloud.png')


text = wiki("alien")
create_wordcloud(text)
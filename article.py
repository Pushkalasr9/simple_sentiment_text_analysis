from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')


url="https://timesofindia.indiatimes.com/nri/us-canada-news/indian-origin-executive-dies-after-assault-washington-street-incident/articleshow/107572930.cms"
article=Article(url)

article.download()
article.parse()
article.nlp()

text=article.summary
print(text)

blob=TextBlob(text)
sentiment=blob.sentiment.polarity # -1 to 1
print(sentiment)

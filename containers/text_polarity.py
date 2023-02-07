import nltk
from textblob import TextBlob


# first download punkt for nltk then comment below line otherwise it will give an error
nltk.download('punkt')

def text_polarity(text=''):
    blob = TextBlob(text)
    return f'Sentiment[Polarity={blob.polarity}]: {"Positive" if blob.polarity > 0 else "Negative" if blob.polarity < 0 else "Neutral"}'
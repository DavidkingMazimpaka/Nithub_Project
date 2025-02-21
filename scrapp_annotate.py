import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    sentences = []
    
    for paragraph in soup.find_all('p'):
        sentences.extend(paragraph.text.split('. '))
    
    return sentences[:200]

def annotate_sentences(sentences):
    sid = SentimentIntensityAnalyzer()
    annotated_sentences = []

    for sentence in sentences:
        sentiment = sid.polarity_scores(sentence)
        if sentiment['compound'] >= 0.05:
            label = 'positive'
        elif sentiment['compound'] <= -0.05:
            label = 'negative'
        else:
            label = 'neutral'
        annotated_sentences.append((sentence, label))
    
    return annotated_sentences

if __name__ == '__main__':
    url = 'https://www.bbc.com/news/articles/clyz6e9edy3o'
    sentences = scrape_news(url)
    annotated_sentences = annotate_sentences(sentences)
    df = pd.DataFrame(annotated_sentences, columns=['Sentence', 'Sentiment'])
    print(df)
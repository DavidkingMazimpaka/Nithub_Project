from textblob import TextBlob

def annotate_sentences_light(sentences):
    annotated_sentences = []

    for sentence in sentences:
        blob = TextBlob(sentence)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            label = 'positive'
        elif sentiment < 0:
            label = 'negative'
        else:
            label = 'neutral'
        annotated_sentences.append((sentence, label))
    
    return annotated_sentences
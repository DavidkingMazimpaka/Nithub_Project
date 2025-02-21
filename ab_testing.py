import random
from flask import Flask, request, jsonify
from scrapp_annotate import scrape_news, annotate_sentences
from optimize_model import annotate_sentences_light

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.get_json(force=True)
    url = data['url']
    sentences = scrape_news(url)
    model_type = random.choice(['baseline', 'optimized'])

    if model_type == 'baseline':
        annotated_sentences = annotate_sentences(sentences)
    else:
        annotated_sentences = annotate_sentences_light(sentences)
    
    response = {
        'model_type': model_type,
        'results': annotated_sentences
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from annotate_sentences import annotate_sentences

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.get_json(force=True)
    sentences = data['sentences']
    annotated_sentences = annotate_sentences(sentences)
    return jsonify(annotated_sentences)

if __name__ == '__main__':
    app.run(debug=True)
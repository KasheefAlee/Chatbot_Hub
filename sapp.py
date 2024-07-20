from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

# Load the model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Home route to serve the web interface
@app.route('/')
def index():
    return render_template('SA_index.html')

# API route for sentiment analysis
@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=-1).tolist()[0]
    sentiment = 'positive' if probabilities[1] > probabilities[0] else 'negative'

    return jsonify({
        'text': text,
        'sentiment': sentiment,
        'probabilities': probabilities
    })

if __name__ == '__main__':
    app.run(debug=True,port=6060)

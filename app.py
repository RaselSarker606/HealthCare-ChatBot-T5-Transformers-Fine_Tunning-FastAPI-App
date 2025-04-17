from flask import Flask, request, jsonify, render_template
from transformers import T5ForConditionalGeneration, T5Tokenizer
import re
# pip install flask transformers torch sentencepiece

app = Flask(__name__)

# Load the saved model +token
model = T5ForConditionalGeneration.from_pretrained('model +token')
tokenizer = T5Tokenizer.from_pretrained('model +token')

device = model.device


# Clean the text by removing unwanted characters
def clean_text(text):
    text = re.sub(r'\r\n', ' ', text)  # Remove carriage returns and line breaks
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'<.*?>', '', text)  # Remove any XML tags
    text = text.strip().lower()  # Strip and convert to lower case
    return text

def chatbot(query):
    query = clean_text(query)
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding="max_length", max_length=250).to(model.device)
    terget_ids = model.generate(inputs.input_ids, max_length=250, num_beams=5, early_stopping=True)
    return tokenizer.decode(terget_ids[0], skip_special_tokens=True)

# Rendering Index Root
@app.route('/')
def index():
    return render_template("index.html")

# API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error 404": "Please enter a message"})
    response = chatbot(user_message) # uporer function dekho
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
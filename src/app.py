from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def extract_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Za-z0-9-]{2,7}\b"
    raw_emails = re.findall(pattern, text)
    emails = [email.lower() for email in raw_emails]
    return emails

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_emails', methods=['POST'])
def extract_emails_route():
    data = request.get_json()
    text = data.get('text', '')
    emails = extract_emails(text)
    return jsonify({'emails': emails})

if __name__ == '__main__':
    app.run(debug=True)
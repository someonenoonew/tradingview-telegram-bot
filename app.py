from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/')
def home():
    return 'Server activ!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    mesaj = data.get('message', 'Alertă fără mesaj')

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': mesaj
    }
    r = requests.post(url, data=payload)
    return 'Trimis', r.status_code

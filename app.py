from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    print(f"Chat ID-ul grupului este: {chat_id}")
    return "OK"

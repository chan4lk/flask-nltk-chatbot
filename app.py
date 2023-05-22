from flask import Flask, request
from chatbot import chat

app = Flask(__name__)

@app.route("/")
def hello_world():
    text = request.args.get('text')
    output = chat(text)
    return f'<h1>{output}!</h1>'
from flask import Flask, request
from chatbot import chat
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route("/")
def hello_world():
    text = request.args.get('text')
    if text is None:
        return "Please send <strong>text</strong> parameter"
    output = chat(text)
    return f'<h1>{output}!</h1>'

@app.route("/message")
def message():
    text = request.args.get('text')
    if text is None:
        return {
        "response": "Please send {text} parameter"
    }
    output = chat(text)
    return {
        "response": output
    }
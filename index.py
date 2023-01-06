from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/saludo')
def saludo():
    return 'Wenas chavales!'


@app.route('/despedida')
def despedida():
    return 'Adiós chavales!'
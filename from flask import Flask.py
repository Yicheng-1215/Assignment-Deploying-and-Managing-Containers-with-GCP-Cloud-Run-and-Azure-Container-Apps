from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App!</h1><p>Random number: {}</p>".format(random.randint(1, 100))

@app.route('/hello')
def hello():
    return "<h1>Hello, Cloud!</h1><p>This is a new route.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

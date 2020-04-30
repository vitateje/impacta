from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! - Hacking NASA'

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)
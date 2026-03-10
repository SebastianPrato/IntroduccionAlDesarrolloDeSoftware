from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

if __name__ == '__main__':
   # esto solo funca usando python3 app.py
   app.run("localhost", port=8081, debug=True)
   
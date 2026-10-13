from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html'), 200

# flask --app leafletdemo.server run

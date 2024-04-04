from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/posts")
def posts():
    return render_template('posts/index.html')
# flask --app server run --debug --port 5000
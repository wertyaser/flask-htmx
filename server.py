from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/users")
def users():
    return render_template('users/index.html')

@app.route("/cashier")
def cashier():
    return render_template('cashier/index.html')

# @app.route("/logout")
# def logout():
#     return render_template('logout/index.html')

# flask --app server run --debug --port 5000
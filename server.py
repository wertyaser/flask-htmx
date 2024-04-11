from flask import Flask, render_template, request
from .db import sample_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/users")
def users():
    users = sample_db.get_users()
    return render_template('users/index.html', users=users)

@app.route("/users/edit/<string:user_id>", methods=['GET', 'PUT'])
def edit_user(user_id):

    #default get req
    user = sample_db.get_user(user_id)
    return render_template('users/_partials/edit.html', user = user)

@app.route("/cashier")
def cashier(): 
    return render_template('cashier/index.html')

@app.route("/monitoring")
def monitoring(): 
    return render_template('monitoring/index.html')



# @app.route("/logout") 
# def logout():
#     return render_template('logout/index.html')

# flask --app server run --debug --port 5000
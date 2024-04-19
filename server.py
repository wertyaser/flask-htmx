from flask import Flask, render_template, request
from flask_mysqldb import MySQL

# Old db
# from .db import sample_db

app = Flask(__name__)

#MSQL CONFIG
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'queue_db'

mysql = MySQL(app)

@app.route("/")
def login():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM your_table")
    data = cur.fetchall()
    cur.close()
    return str(data)

# @app.route("/home")
# def home():
#     return render_template('home/index.html')

# @app.route("/users")
# def users():
#     users = sample_db.get_users()
#     return render_template('users/index.html', users=users)

# @app.route("/user/<string:user_id>")
# def show(user_id):
#     user = sample_db.get_user(user_id)
#     return render_template('users/_partials/show.html', user=user)

# @app.route("/users/edit/<string:user_id>", methods=['GET', 'PUT'])
# def edit_user(user_id):
#     if request.method == 'PUT':
#         name = request.form.get('name')
#         type = request.form.get('type')
#         sample_db.update_user(user_id, name=name, type=type)
#         return show(user_id)
    
#     #default get req
#     user = sample_db.get_user(user_id)
#     return render_template('users/_partials/edit.html', user = user)

# @app.route("/cashier")
# def cashier(): 
#     return render_template('cashier/index.html')

# @app.route("/monitoring")
# def monitoring(): 
#     return render_template('monitoring/index.html')



# @app.route("/logout") 
# def logout():
#     return render_template('logout/index.html')

# flask --app server run --debug --port 5000
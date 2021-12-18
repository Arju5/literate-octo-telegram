from flask import Flask,render_template

app = Flask(__name__) #__name__ is a builtin variable can always call from any py file refering to local py working file

@app.route("/") #Decorator - one step before func like end point
@app.route("/home") #Decorator - one step before func like end point
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)

@app.route("/about/<username>")
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'
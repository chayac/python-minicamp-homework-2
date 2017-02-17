# Initialize Flask
from flask import Flask, render_template, jsonify

app = Flask(__name__)


# Setup your initial route at `/` to return `'Hello World'`.
# Modify your home route (`/`) to return the html template provided below.
@app.route('/')
def index():
    return render_template('home.html')


# Build a route called `/birthday` that returns your birthday as a `string`
# in this format: `'October 30 1911'`.
@app.route('/birthday')
def birthday():
    return str('February 15 1987')


# Build a route called `/greeting` that accepts a parameter called `name`.
# The route should return a string that says `'Hello <name>'`
# where `<name>` is the name that you passed to the route.
@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name.capitalize()


# Create a route called `/add` that adds two parameteres together and returns them.
@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    try:
        total = int(num1) + int(num2)
        return str(total)
    except ValueError:
        return 'Please enter two integer values'


# Create a route called `/multiply` and a route called `/subtract`
@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    try:
        total = int(num1) * int(num2)
        return str(total)
    except ValueError:
        return 'Please enter two integer values'


@app.route('/subtract/<num1>/<num2>')
def subtract(num1, num2):
    try:
        total = int(num1) - int(num2)
        return str(total)
    except ValueError:
        return 'Please enter two integer values'


# Create a route called `/favoritefoods` that returns a `list` of your favorite foods
@app.route('/favoritefoods')
def favoritefoods():
    list_favorite_foods = ['pizza', 'tacos', 'sushi']
    return jsonify(list_favorite_foods)

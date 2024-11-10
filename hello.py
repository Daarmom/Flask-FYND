from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello World!</p>"
@app.route("/")
def homepage():
    return render_template('homepage.html')

# @app.route("/products/")
# def products():
#     return "<h1>Products</h1>"

@app.get("/products/")
def products_get():
    return "<h1>Products</h1>"

@app.post("/products/")
def products_post():
    return "This is post call"
    
# @app.route("/products/", methods=['GET', 'POST'])
# def products():
#     if request.method == 'POST':
#         return "THis is post call"
#     else:
#         return "<h1>Products</h1>"

# @app.route("/products/<int:id>/")
# def product(id):
#     # return f"<h1>Product: #{id}</h1>"
#     return f"<h1>Product: #{escape(id)}</h1>"

@app.route("/products/<int:id>/")
def product(id):
    return render_template('products.html', productid = id)

@app.route("/hello/")
@app.route("/hello/<name>/")
def greet(name = None):
    return render_template('greet.html', name = name)

@app.route("/users/")
def users():
    firstName = request.args.get('fname')
    lastName = request.args.get('lname')
    print(request.args)
    return f"<h1>Users page: {firstName} {lastName}</h1>"

@app.route("/users/<username>/")
def user(username):
    return f"<h1>User: #{escape(username)}</h1>"

@app.route("/path/<path:subpath>/")
def path(subpath):
    return f"<h1>Path: #{escape(subpath)}</h1>"

@app.route("/about-us/")
def abouts():
    return "<h1>ABOUT US</h1>"

@app.route("/forms/")
def form():
    return ''''''
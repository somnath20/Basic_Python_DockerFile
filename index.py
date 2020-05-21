from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/index')
def index():
    user = {'username': 'Somnath'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/about')
def about():
    return "<h1>About Page for Hello World</h1>"


if __name__ == '__main__':
    app.run(debug=True)

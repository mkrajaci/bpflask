from flask import Flask

app = Flask(__name__)


# rute do stranica
@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello World!!!</h1>'

@app.route('/about')
def about():
    return '<h1>About page</h1>'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

__author__ = 'Nikhil'

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():
    return render_template("index.html", title='Test')


if __name__ == '__main__':
    app.run()

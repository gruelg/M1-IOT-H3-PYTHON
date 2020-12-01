from flask import Flask, render_template
from flask import request
import json

app = Flask(__name__)

#books = json.load(open('books.json'))

@app.route('/api/books')
def fBooks():
    return books

@app.route('/<name>')
def hello(name=None):
    return render_template('tpl1.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)


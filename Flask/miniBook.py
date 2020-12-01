from flask import Flask, render_template
from flask import request
import flask
import json

app = Flask(__name__)

books = json.load(open('books.json'))

@app.route('/api/books')
def fBooks():
   books = json.load(open('books.json'))
   return flask.jsonify(books)

@app.route('/<id>')
def idBook(id ):
    books = json.load(open('books.json'))
    return render_template('book.html', contenu=books[int(id)])

@app.route('/titre/<titre>')
def titleBook(titre ):
    books = json.load(open('books.json'))
    for i in range(len(books)):
        if books[i]['title'] == titre:
            return render_template('book.html', contenu = books[i])

@app.route('/id', methods = ['POST', 'GET'])
def idBookForm():
    books = json.load(open('books.json'))
    id = request.form['id']
    return flask.jsonify(books[int(id)])
    return render_template('book.html', contenu=books[int(id)])

@app.route('/titre/', methods = ['POST', 'GET'])
def titleBookForm():
    books = json.load(open('books.json'))
    titre = request.form['title']
    for i in range(len(books)):
        if books[i]['title'] == titre:
            return render_template('book.html', contenu = books[i])

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

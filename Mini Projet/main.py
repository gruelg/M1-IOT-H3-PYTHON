from flask import Flask, render_template
import os
from flask import request
import flask
import json
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('base.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projet')
def projet():
    projet = json.load(open('projet.json'))
    #return flask.jsonify(projet)
    return render_template('projet.html', projets=projet)


if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000))
    #host='172.0.0.1'
    #app.run(host=host, port=port)
    app.run(debug=True)
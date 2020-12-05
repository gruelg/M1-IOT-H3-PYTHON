from flask import Flask, render_template, redirect, url_for
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

@app.route('/contact', methods=['POST'])
def text_box():
    response = {}
    response['nom'] = request.form['nom']
    response['prenom'] = request.form['prenom']
    response['mail'] = request.form['mail']
    response['message'] = request.form['message']
    with open('messages.json', 'w') as f:
        json.dump(response, f, indent=4, ensure_ascii=False, sort_keys=False)
    return render_template('base.html')

@app.route('/projet')
def projet():
    projet = json.load(open('projet.json'))
    #return flask.jsonify(projet)
    return render_template('projet.html', projets=projet)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
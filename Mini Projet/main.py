from flask import Flask, render_template
import os
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

if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000))
    #host='172.0.0.1'
    #app.run(host=host, port=port)
    app.run(debug=True)
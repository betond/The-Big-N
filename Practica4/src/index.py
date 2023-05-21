from flask import Flask, render_template
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route('/')
def signIn():
    return render_template('signIn.html')

@app.route('/signup')
def signUp():
    return render_template('signUp.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)
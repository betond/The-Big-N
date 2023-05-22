from flask import Flask, render_template, request, redirect, url_for
import os
import hashlib
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def signIn():
    #cursor = db.database.cursor()
    #cursor.execute("SELEC * FROM user")
    #cursor.close
    return render_template('signin.html')

#registro de usuarios
@app.route('/signup', methods=['POST'])
def signUp():
    #username = request.form['username']
    #password = request.form['password']
    #email = request.form['email']
    
    #if username and password and email:
    #    hash = hashlib.sha224(password.encode)
    #    val = 'T'
    #    cursor = db.database.cursor()
    #    sql = "INSERT INTO user (username, hpassword, email, val) VALUES (%s, %s, %s, %s)"
    #    data = (username, hash, email, val)
    #    cursor.execute(sql, data)
    #    db.database.commit()
    #    return render_template('home.html')
        
    return render_template('signUp.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/lostpass')
def lostpass():
    return render_template('lostpass.html')

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, render_template


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
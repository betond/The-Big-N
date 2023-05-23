from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config
# Models:
from models.ModelUser import ModelUser
# Entities:
from models.entities.User import User

app = Flask(__name__)


#csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('signIn'))

@app.route('/signin', methods=['GET','POST'])
def signIn():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta...")
                return render_template('signIn.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('signIn.html')
    else:
        return render_template('signIn.html')


@app.route('/verificacion', methods=['GET','POST'])
def VerEmail():
    if request.method == 'POST':
        return render_template('VerEmail.html')
    else:
        return render_template('VerEmail.html')

@app.route('/home', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        return render_template('home.html')

@app.route('/lostpass', methods=['GET','POST'])
def lostpass():
    if request.method == 'POST':
        return render_template('lostpass.html')   
    else:
        return render_template('lostpass.html')

#registro de usuarios
@app.route('/signup', methods=['GET','POST'])
def signUp():
    
    if request.method == 'POST':
        return render_template('signUp.html')
    else:    
        return render_template('signUp.html')
 
    
@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('signIn'))

def status_401(error):
    return redirect(url_for('signIn'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])
#    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
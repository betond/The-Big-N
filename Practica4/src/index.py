from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from models.smtp.correo import SendCorreo
import random, string

from config import config
# Models:
from models.ModelUser import ModelUser
# Entities:
from models.entities.User import User

code = ''
leng = int(8)

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

@app.route('/home')
@login_required
def home():
        return render_template('home.html')

@app.route('/lostpass', methods=['GET','POST'])
def lostpass():
    global code
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['npass'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if request.form['codigoVer'] != '':
                if code == request.form['codigoVer']:
                    username = request.form['username']
                    hpassword = generate_password_hash(request.form['npass'])              
                    sql = f"UPDATE user SET hpassword = '{hpassword}' WHERE username = '{username}'"
                    db.connection.cursor().execute(sql)
                    db.connection.commit()
                    return redirect(url_for('signIn'))
                else:
                    flash("Codigo de verificación incorrecto.")
                    return redirect(url_for('lostpass'))
            else:
                user = User(0, request.form['username'],'', '')
                search_user = ModelUser.login(db, user)
                if search_user.email:
                    email = search_user.email
                    ver = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(leng))
                    code = ver
                    msg = "El codigo de recuperación de contraseña es: " + code
                    SendCorreo(email, msg,"Verificación de email.")
                    flash("Ingrese los datos de nuevo e ingresa el codigo de verificación. ")
                    return redirect(url_for('lostpass'))

        else:
            flash("Usuario no encontrado...")
            return render_template('lostpass.html')   
    else:
        return render_template('lostpass.html')

#registro de usuarios
@app.route('/signup', methods=['GET','POST'])
def signup():
    
    if request.method == 'POST':
        global code
        if request.form['codigoVer'] != '':
            if code == request.form['codigoVer']:
                username = request.form['username']
                hpassword = generate_password_hash(request.form['password'])
                email = request.form['email']
                sql = f"INSERT INTO user (username, hpassword, email) VALUES ('{username}','{hpassword}','{email}')"
                db.connection.cursor().execute(sql)
                db.connection.commit()
                return redirect(url_for('home'))
            else:
                flash("Codigo de verificación incorrecto.")
                return redirect(url_for('signup'))
        else:
            username = request.form['username']
            hpassword = generate_password_hash(request.form['password'])
            email = request.form['email']
            ver = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(leng))
            code = ver
            msg = "El codigo de verificación es: " + code
            SendCorreo(email, msg,"Verificación de email.")
            flash("Ingrese los datos de nuevo y verificar correo electronico. ")
            return redirect(url_for('signup'))
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
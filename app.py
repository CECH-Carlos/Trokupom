from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow
from pyrebase import initialize_app
from config import firebaseConfig, path_on_cloud, path_local, ALLOWED_EXTENSIONS, admin_list
from flask_socketio import SocketIO, emit, send
from datetime import datetime

from models.tables import Produto, User, user_share_schema, users_share_schema

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

io = SocketIO(app)
firebase = initialize_app(firebaseConfig)
auth = firebase.auth()
uploads = firebase.storage()

messages = []

@app.shell_context_processor
def shell_context_processor():
    return dict(
        app=app, 
        db=db, 
        User=User
    )

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/chat", methods=['GET', 'POST'])
def chat():
    return render_template("chat.html")

@app.route("/produto", methods=['GET', 'POST'])
def produto():
    return render_template("produto.html")

@app.route("/postProduto", methods=['GET', 'POST'])
def addProduto():
    return render_template("addProduto2.html")

@app.route("/auth/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try: 
            auth.sign_in_with_email_and_password(email, password)
            #TODO: Pensar em como deixar o usuário com a função de login_user(user) -> descobrir como utilizar e redirecionar a página
            user = User.query.filter_by(email=email).first()
            flash("Logged in.")

            if email in admin_list:
                return redirect(url_for('/admin', code=302))

            return redirect(url_for('/home', code=302))
        except:
            flash("Please check your credentials.")
    
    return render_template("login.html")

@app.route("/auth/cadastro", methods=['GET', 'POST'])
def cadastro():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']

        auth.create_user_with_email_and_password(email, password)

        now = datetime.now()
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")


        if email in admin_list:
            admin = True
        else:
            admin = False


        user = User(
            username,
            password,
            name, 
            email,
            admin,
            created_at,
            updated_at
        )

        db.session.add(user)
        db.session.commit()

        return redirect('/auth/login', code=302)

    return render_template('cadastroPage.html')

@app.route("/auth/login/resetPassword", methods=['POST'])
def rememberme():

    if request.method == 'POST':   
        email = request.form['email']

        auth.send_password_reset_email(email)

        user = User.query.get(email)

        now = datetime.now()
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        
        user.updated_at = updated_at
        db.session.commit()
        
        return redirect(url_for('login'), code=302)
    
    return render_template('resetPassword.html')

@app.route('/postProduto', methods=['GET', 'POST'])
def upload_image():
    
    if request.method == 'POST':
        name = request.form['nome-produto']
        comentario = request.form['comentario']
        categoria = request.form['categoria']
        image = request.form['imagem']

        path_local = f'uploads-dos-usuarios/{image}'

        uploads.child(path_on_cloud).put(path_local)

        produto = Produto(
            name, 
            comentario,
            categoria
        )

        db.session.add(produto)
        db.session.commit()

        return redirect('/home', code=302)

    return render_template('addProduto2.html')


@io.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg)
    emit('getMessage', msg, broadcast=True)

@io.on('message')
def message_handler(msg):
    send(messages)

if __name__ == "__main__":
    app.run()
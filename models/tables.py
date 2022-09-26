from sqlalchemy import ForeignKey
from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash

# TODO: mudar o tipo do id de Integer para String


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    admin = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    #TODO: Mudar a Página de Cadastro para poder comportar isso + recriar os usuários já criados no banco de dados.
    #interesse_id = db.Column(db.Integer, db.ForeignKey('interesses.id'), nullable=False)

    #interesse = db.relationship('Interesses', foreign_key=interesse_id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email, admin, created_at, updated_at):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
        self.email = email
        self.admin = admin
        self.created_at = created_at
        self.updated_at = updated_at

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User %r>" % self.username


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email')


user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(145))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "followers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    follower_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)


class Troca(db.Model):
    __tablename__ = "trocas"

    id = db.Column(db.Integer, primary_key=True)
    transacao = db.Column(db.Boolean)
    dataInicio = db.Column(db.DateTime)
    dataFim = db.Column(db.DateTime)
    status = db.Column(db.String(45))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    troca_id = db.Column(db.Integer, db.ForeignKey(
        'trocas.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)
    troca = db.relationship('Troca', foreign_keys=troca_id)


class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    #usado = db.Column(db.Boolean)
    comentario = db.Column(db.String(95))
    categoria = db.Column(db.String(45), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    troca_id = db.Column(db.Integer, db.ForeignKey('trocas.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)
    troca = db.relationship('Troca', foreign_keys=troca_id)

    def __init__(self, name, comentario, categoria):
        self.name = name
        self.comentario = comentario
        self.categoria = categoria

    def __repr__(self):
        return "<Produto %r>" % self.name
class Interesses(db.Model):
    _tablename_ = "interesses"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    interesse = db.Column(db.String(45), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)

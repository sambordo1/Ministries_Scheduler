import imp, json, time, os, re

from flask import Flask, request, session, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sock import Sock

app = Flask(__name__)
app.secret_key = b'woohoo!_random_secret_key_;-)'

path = os.path.dirname(os.path.realpath(__file__))
database_path = os.path.join(path, 'backend.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
sock = Sock(app)


@app.cli.command('initdb')
def initdb():
    db.drop_all()
    db.create_all()
    # TODO any additional setup


ministries = db.Table('ministries',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('ministry_id', db.Integer, db.ForeignKey('ministry.id'), primary_key=True),
)

user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    ministries = db.relationship('Ministry', secondary=ministries, lazy='subquery',
        backref=db.backref('users', lazy='dynamic'))
    roles = db.relationship('Role', secondary=user_roles, lazy='subquery',
        backref=db.backref('users', lazy='dynamic'))
    
    def __repr__(self):
        return f'<User {self.username}>'


class Ministry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    roles = db.relationship('Role', backref='ministry', lazy='dynamic')

    def __repr__(self):
        return f'<Message {self.name}>'


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    ministry_id = db.Column(db.Integer, db.ForeignKey('ministry.id'), nullable=False)

    def __repr__(self):
        return f'<Message {self.name}>'


@app.route("/")
def wasm_frontend():
    return render_template('appscheduler_frontend.html')

@app.route("/<path:path>")
def get_resource(path):
    # TODO filter to only expected resources
    return send_from_directory('static', path)

@sock.route("/ws")
def ws_handler(sock):
    while True:
        # TODO send message handling to other methods
        data = sock.receive()
        sock.send(data)

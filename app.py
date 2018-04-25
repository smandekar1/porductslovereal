import re
import os
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from config import Config

#ss
app = Flask(__name__)

app.debug = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/flaskhawkes'
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

       
    

@app.route('/')
def homepage():
    html = render_template('homepagenew.html')
    return html


@app.route('/contact')
def contact():

    html = render_template('contactnew.html')
    return html


@app.route('/books')
def books():
    html = render_template('books.html', title=contact)
    return html

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('homepagenew'))


if __name__ == '__main__':
    
    db.create_all()

    port = int(os.environ.get("PORT", 33507))
    app.run(
        host="0.0.0.0",
        port=port,
    )
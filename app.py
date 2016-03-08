from flask import Flask, jsonify, render_template
import sqlite3
from contextlib import closing
from endpoints import api


DATABASE = 'main.db'
Debug = True
SECRET_KEY = 'devkey'
USERNAME = 'admin'
PASSWORD = 'password'


app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(api, url_prefix='/api/v1')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db


@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

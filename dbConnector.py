from flask import Flask, jsonify, render_template
import sqlite3
from contextlib import closing

DATABASE = 'main.db'
Debug = True
SECRET_KEY = 'devkey'
USERNAME = 'admin'
PASSWORD = 'password'


def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with closing(connect_db()) as db:
        with open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = connect_db()
#     return db

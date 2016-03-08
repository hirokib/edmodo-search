from flask import Flask, jsonify, render_template, Blueprint
from dbConnector import connect_db
from flask import json, Response, request

api = Blueprint('api', __name__, template_folder='templates')

def query_db(query, args=(), one=False):
    cur = connect_db().cursor()
    cur.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return (rv[0] if rv else None) if one else rv


@api.route('/products', methods=['GET'])
def getAllProducts():
    prods = query_db('select * from products')
    prods = json.dumps(prods)
    resp = Response(response=prods, mimetype='application/json')
    return resp

@api.route('/products/<search>', methods=['GET'])
def getSearchResults(search):
    if len(search) < 3:
        query = "select products._id, products._score, _source.title, _source.img_path, \
        _source.long_desc from  products inner join _source on products._id = _source.product_id where \
          _source.title like \'{}%\'".format(search)
    else:
        query = "select products._id, products._score, _source.title, _source.img_path, \
        _source.long_desc from products inner join _source on products._id = _source.product_id \
        where _source.title like \'%{0}%\' or _source.long_desc  like\'%{0}%\'".format(search)
    prods = query_db(query)
    prods = json.dumps(prods)
    resp = Response(response=prods, mimetype='application/json')
    return resp

@api.route('/search-result-flags', methods=['POST'])
def parseRanking():
    data = request.data
    res = json.loads(data.decode('utf-8'))
    print(res)
    return 'success'

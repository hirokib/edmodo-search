from flask import Flask, jsonify, render_template, Blueprint
from dbConnector import connect_db
from flask import json, Response, request

api = Blueprint('api', __name__, template_folder='templates')

def query_db(query, args=(), one=False):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    conn.close()
    return (rv[0] if rv else None) if one else rv

def execute_query(queries):

    for q in queries:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(q)
        conn.commit()
        conn.close()
    return 'executed'

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
        _source.long_desc, _source.price from products inner join _source on products._id = _source.product_id \
        where _source.title like \'%{0}%\' or _source.long_desc  like\'%{0}%\'".format(search)
    prods = query_db(query)
    prods = json.dumps(prods)
    resp = Response(response=prods, mimetype='application/json')
    return resp

@api.route('/search-result-flags', methods=['POST'])
def parseRanking():
    data = request.data
    res = json.loads(data.decode('utf-8'))
    query = res['query']
    prod_id = res['id']
    inappropriate  = 1 if (res['resultFlags']['modalValue1']) else 0
    nothelpful  = 1 if (res['resultFlags']['modalValue2']) else 0
    wrongtags  = 1 if (res['resultFlags']['modalValue3']) else 0
    spam  = 1 if (res['resultFlags']['modalValue4']) else 0
    if (inappropriate == 0 and nothelpful == 0 and wrongtags == 0 and spam == 0):
        return
    print(query)
    print(prod_id)
    # if update succeeds, correct incrementing. otherwise nothing will happen
    # implying key does not exist so the next statement will insert new row
    # making up for lack of upsert
    dbquery = "UPDATE searchRatings SET inappropriate = inappropriate+{0},nothelpful = nothelpful+{1}, \
                wrongtags=wrongtags+{2},spam=spam+{3} WHERE (query = \'{4}\' and \
                product_id = {5})".format(inappropriate, nothelpful, wrongtags, spam, query, prod_id)
    dbquery1 = "INSERT OR IGNORE INTO searchRatings (query, product_id, inappropriate, nothelpful, wrongtags, spam) \
             VALUES (\'{4}\',{5},{0},{1},{2},{3})".format(inappropriate, nothelpful, wrongtags, spam, query, prod_id)

    print(dbquery, dbquery1)
    execute_query([dbquery, dbquery1])

    return 'success'

@api.route('/products/flagged', methods=['GET'])
def getFlaggedResults():
    query = "select s.title, sr.product_id, sr.query, sr.inappropriate, sr.nothelpful, sr.wrongtags, \
            sr.spam from searchRatings as sr,  _source as s where s.product_id = sr.product_id;"
    result = query_db(query)
    print('flagged called')
    print(result)
    json_result = json.dumps(result)
    resp = Response(response=json_result, mimetype='application/json')
    return resp

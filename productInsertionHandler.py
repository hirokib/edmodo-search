import sqlite3
from app import app
from requestHandler import getProductsFromQueries, readQueryFileToList

TEST_DATA = {
    '_index': 'edmarket_prod_321',
    '_id': '306971',
    'sort': [0.3970431, None],
    'fields': {'edm_score': [0.0], 'subject_taxonomy': [11, 17], 'is_shared': [True], 'content_type': [1], 'img_path': ['https://media-market.edmodo.com/media/public/3022362eb875aa85bb2b97a049e6c7a8ea2b3399.png'], 'greads_review_url': [''], 'grades': ['Not Grade Specific'], 'nor_avg_rating': [0.0], 'num_raters': [0], 'usage_rights': [4], 'min_price': [0.0], 'title': ['math'], 'long_desc': [''], 'currency': ['USD'], 'avg_rating': [0.0], 'amazon_tags': [''], 'resource_types': ['Web Link', 'Collection'], 'long_desc_html': [''], 'seller_thumb_url': ['https://api.edmodo.com/users/68065005/avatar?type=small&u=j79ncrf8nrsrio2zp9qh8pqa'], 'url': ['math,306971/'], 'creation_date': ['2015-04-13T00:00:00.000Z'], 'price': [0.0], 'nor_num_raters': [0]},

    '_source': {
        'edm_score': 0,
        'languages': [],
        'subject_taxonomy': [11, 17],
        'cc_tags': [],
        'is_shared': True,
        'content_type': 1,
        'id': 306971,
        'img_path': 'https://media-market.edmodo.com/media/public/3022362eb875aa85bb2b97a049e6c7a8ea2b3399.png',
        'greads_review_url': '',
        'currency': 'USD',
        'nor_avg_rating': 0.0,
        'num_raters': 0,
        'usage_rights': 4,
        'min_price': 0.0,
        'long_desc': '',
        'title': 'math',
        'liked': False,
        'tags': [],
        'grades': ['Not Grade Specific'],
        'avg_rating': 0.0,
        'amazon_tags': '',
        'resource_types': ['Web Link', 'Collection'],
        'img_has_other_size': False,
        'long_desc_html': '',
        'seller_thumb_url': 'https://api.edmodo.com/users/68065005/avatar?type=small&u=j79ncrf8nrsrio2zp9qh8pqa',
        'owner': {
            'school_id': 0,
            'followers': 0,
            'store_url': '/profile/andover-education-publisher,68065005/',
            'edmodo_url': 'https://api.edmodo.com/users/68065005',
            'district_id': 0,
            'id': 68065005,
            'last_name': 'Publisher',
            'thumb_url': 'https://api.edmodo.com/users/68065005/avatar?type=small&u=j79ncrf8nrsrio2zp9qh8pqa',
            'type': 'publisher',
            'first_name': 'Andover Education'},
        'url': 'math,306971/',
        'creation_date': '2015-04-13T00:00:00',
        'price': 0.0,
        'nor_num_raters': 0},
    '_type': 'product',
    '_score': 0.3970431}

def deleteAllTableContents():
    conn = sqlite3.connect('main.db', timeout=30)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM _source")
    cursor.execute("DELETE FROM owner")
    conn.commit()
    conn.close()

def insertProductIntoDB(product):
    index = product['_index']
    print(index)
    product_id    = product['_id']
    print(product_id)
    product_type  = product['_type']
    print(product_type)

    score = product['_score']
    print(score)

    ''' begin source items '''
    source              = product['_source']
    product_id          = source['id']
    title               = source['title']
    min_price           = source['min_price']
    long_desc           = source['long_desc']
    nor_avg_rating      = source['nor_avg_rating']
    num_raters          = source['num_raters']
    price               = source['price']
    usage_rights        = source['usage_rights']
    currency            = source['currency']
    owner_id            = source['owner']['id']
    edm_score           = source['edm_score']
    content_type        = source['content_type']
    is_shared           = source['is_shared']
    url                 = source['url']
    long_desc_html      = source['long_desc_html']
    liked               = source['liked']
    img_path            = source['img_path']
    nor_num_raters      = source['nor_num_raters']
    creation_date       = source['creation_date']
    img_has_other_size  = source['img_has_other_size']
    greads_review_url   = source['greads_review_url']
    ''' end source items '''

    ''' begin owner items '''
    owner       = source['owner']
    owner_id    = owner['id']
    thumb_url   = owner['thumb_url']
    district_id = owner['district_id']
    first_name  = owner['first_name']
    owner_type  = owner['type']
    store_url   = owner['store_url']
    print(store_url)
    followers   = owner['followers']
    print(followers)
    last_name   = owner['last_name']
    print(last_name)
    edmodo_url  = owner['edmodo_url']
    school_id   = owner['school_id']
    ''' end owner itmes '''


    conn = sqlite3.connect('main.db', timeout=30)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (_id, _index, _score, _type) \
        VALUES (?,?,?,?)", (product_id, index, score, product_type))
    cursor.execute("INSERT INTO _source (product_id, title, min_price, long_desc, nor_avg_rating, num_raters, price, \
        usage_rights, currency, owner, edm_score, content_type, is_shared, url, long_desc_html, \
        liked, img_path, nor_num_raters, creation_date, img_has_other_size, greads_review_url) \
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (product_id, title, min_price, long_desc, nor_avg_rating, num_raters, price, \
        usage_rights, currency, owner_id, edm_score, content_type, is_shared, url, long_desc_html,
        liked, img_path, nor_num_raters, creation_date, img_has_other_size, greads_review_url))

    conn.commit()
    conn.close()

def dbProductSetup():
    query_list = readQueryFileToList('queryList.txt')
    prods = getProductsFromQueries(query_list)
    for prod in prods:
        insertProductIntoDB(prod)

if __name__ == "__main__":
    dbProductSetup()

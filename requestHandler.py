# _*_ coding:utf-8 _*_

import requests


def getSearchResultsAsJson(url):
    # Takes url as string and returns jsonified response
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.json()


def getProductsFromQueries(query_list):
    # Takes list of url queries and returns their results
    productList = []
    for query in query_list:
        result = getSearchResultsAsJson(query)
        products = result['products']
        for p in products:
            productList.append(p)
    return productList


def readQueryFileToList(file):
    return [line.rstrip() for line in open(file)]

if __name__ == "__main__":
    # req = getSearchResultsAsJson("https://spotlight.edmodo.com/api/search/?q=mitosis")['products']
    # print(req[0].keys())

    query_file = 'queryList.txt'
    query_list = readQueryFileToList(query_file)
    # print(query_list)
    p = getProductsFromQueries(
        ['https://spotlight.edmodo.com/api/search/?q=math'])
    # print(p[0])
    products = getProductsFromQueries(query_list)
    print(products[0])
    # querySet = set()
    # for p in products:
    #     querySet.add(p['_id'])
    # print(products)

import requests
from datetime import datetime
from exchange import Exchange, BCP


def get_dump():
    try:
        api_dump = requests.get("https://dolar.melizeche.com/api/1.0/").json()
    except:
        api_dump = None
        print("Something went wrong")
    updated = datetime.strptime(api_dump['updated'], '%Y-%m-%d %H:%M:%S')
    return api_dump


def get_sources():
    dump = get_dump()
    exchanges = []
    for key, value in dump['dolarpy'].iteritems():
        exchanges.append(key)
    return exchanges


def build_exchanges_list():
    dump = get_dump()
    exchanges = []
    for key, value in dump['dolarpy'].iteritems():
        if key == 'bcp':
            print("SSDF@@@")
            temp = BCP(key, value['compra'], value[
                       'venta'], value['referencial_diario'])
        else:
            temp = Exchange(key, value['compra'], value['venta'])
        exchanges.append(temp)
    return exchanges


def build_exchanges_dict():
    dump = get_dump()
    exchanges = {}
    for key, value in dump['dolarpy'].iteritems():
        if key == 'bcp':
            print("SSDF@@@")
            temp = BCP(key, value['compra'], value[
                       'venta'], value['referencial_diario'])
        else:
            temp = Exchange(key, value['compra'], value['venta'])
        exchanges[key] = (temp)
    return exchanges


def get_all():
    return build_exchanges_dict()

# def get(**kwargs):
#     exchanges = build_exchanges_dict()
#     if('exchange' in kwargs):
#         return
#     else:
#         return exchanges['bcp'].referencial

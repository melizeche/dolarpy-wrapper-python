import requests
from datetime import datetime
from .exchange import Exchange, BCP

DEFAULT_PROVIDER = 'bcp'
API_URL = 'https://dolar.melizeche.com/api/1.0/'


def get_dump():
    """Get raw API output in a dict"""
    try:
        api_dump = requests.get(API_URL).json()
    except:
        api_dump = None
        print("Something went wrong")
    updated = datetime.strptime(api_dump['updated'], '%Y-%m-%d %H:%M:%S')
    return api_dump


def get_providers():
    """Get a list of providers/exchanges"""
    dump = get_dump()
    exchanges = []
    for key, value in dump['dolarpy'].iteritems():
        exchanges.append(key)
    return exchanges


def build_exchanges_list():
    """Returns a Exchange objects list"""
    dump = get_dump()
    updated = datetime.strptime(dump['updated'], '%Y-%m-%d %H:%M:%S')
    exchanges = []
    for key, value in dump['dolarpy'].iteritems():
        if key == 'bcp':
            temp = BCP(key, value['compra'], value[
                       'venta'], value['referencial_diario'], updated)
        else:
            temp = Exchange(key, value['compra'], value['venta'], updated)
        exchanges.append(temp)
    return exchanges


def build_exchanges_dict():
    """Returns a Exchange objects dict"""
    dump = get_dump()
    updated = datetime.strptime(dump['updated'], '%Y-%m-%d %H:%M:%S')
    exchanges = {}
    for key, value in dump['dolarpy'].items():
        if key == 'bcp':
            temp = BCP(key, value['compra'], value[
                       'venta'], value['referencial_diario'], updated)
        else:
            temp = Exchange(key, value['compra'], value['venta'], updated)
        exchanges[key] = (temp)
    return exchanges


def get_all():
    """Get all exchanges in a dict"""
    return build_exchanges_dict()


def get(**kwargs):
    """
    Get a integer with the rate

    Keyword arguments:
    provider -- which provider to use, if not the default
    """
    exchanges = build_exchanges_dict()
    if('provider' in kwargs):
        try:
            return exchanges[kwargs['provider']].compra
        except KeyError:
            return None
    else:
        return exchanges[DEFAULT_PROVIDER].referencial


def get_compra(**kwargs):
    """
    Get a integer with the buy rate

    Keyword arguments:
    provider -- which provider to use, if not the default
    """
    exchanges = build_exchanges_dict()
    if('provider' in kwargs):
        try:
            return exchanges[kwargs['provider']].compra
        except KeyError:
            return None
    else:
        return exchanges[DEFAULT_PROVIDER].compra


def get_venta(**kwargs):
    """
    Get a integer with the sell rate

    Keyword arguments:
    provider -- which provider to use, if not the default
    """
    exchanges = build_exchanges_dict()
    if('provider' in kwargs):
        try:
            return exchanges[kwargs['provider']].venta
        except KeyError:
            return None
    else:
        return exchanges[DEFAULT_PROVIDER].venta

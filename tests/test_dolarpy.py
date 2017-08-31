from dolarpy import get, get_dump

def test_get():
    response = get()
    assert isinstance(response,float)

def test_get_dump():
    response = get_dump()
    assert isinstance(response,dict)

class Exchange(object):

    def __init__(self, nombre=None, compra=None, venta=None, updated=None):
        self.nombre = nombre
        self.compra = compra
        self.venta = venta
        self.updated =  updated

    def __repr__(self):
        return str(self.nombre)


class BCP(Exchange):

    def __init__(self, nombre=None, compra=None, venta=None, referencial=None):
        self.referencial = referencial
        super(BCP, self).__init__(nombre, compra, venta)

from repositorios import Repositorios

class ProductoService:

    def get_productosList(self):
        return Repositorios.productosList


    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        producto_new = int(lastKey) + 1
        Repositorios.productosList[producto_new] = producto.__dict__
        return producto_new

    def update_producto(self, key, producto):
        if key not in Repositorios.productosList:
            raise ValueError("El producto no existe")
        Repositorios.productosList.update({key: producto.__dict__})

    def delete_producto(self, key):
        if key not in Repositorios.productosList:
            raise ValueError("El producto a elminar no existe")
        del Repositorios.productosList[key]

    def insertion_sort_precio(self, listacopia, orden):
        lis = listacopia.copy()
        if orden == 'ascendente':
            for i in range(1, len(lis)):
                valor = lis[i]
                j = i-1
                while j >= 0 and valor['_precio'] < lis[j]['_precio']:
                    lis[j + 1] = lis[j]
                    j -= 1
                lis[j + 1] = valor
            return lis
        if orden == 'descendente':
            for i in range(1, len(lis)):
                valor = lis[i]
                j = i-1
                while j >= 0 and valor['_precio'] > lis[j]['_precio']:
                    lis[j + 1] = lis[j]
                    j -= 1
                lis[j + 1] = valor
            return lis
class Celda:
    __sig = None
    __item = None

    def __init__(self, item = None):
        self.__sig = None
        self.__item = item

    def setItem(self, item):
        self.__item = item
    
    def setSig(self, celda):
        self.__sig = celda

    def getItem(self):
        return self.__item
    
    def getSig(self):
        return self.__sig

class ListaEncadenada:
    __cant = None
    __ul = None
    __cabeza = None

    def __init__ (self):
        self.__cabeza = None
        self.__cant = -1
        self.__ul = None
    
    def vacio(self):
        return self.__cant == -1

    def buscar(self, pos):
        aux = self.__cabeza
        i = 0
        while i < pos-1 or aux.getSig() == None:
            aux = aux.getSig()
            i += 1
        return aux

    def Insertar(self, x, pos):
        pos -= 1
        if 0 <= pos <= self.__cant+1:
            unaCelda = Celda()
            unaCelda.setItem(x)
            if self.__cabeza == None and self.vacio():
                self.__cabeza = unaCelda
                self.__ul = unaCelda
            elif pos == 0:
                unaCelda.setSig(self.__cabeza)
                self.__cabeza = unaCelda
            elif pos == self.__cant+1:
                self.__ul.setSig(unaCelda)
                self.__ul = unaCelda
            elif pos <= self.__cant:
                ant = self.buscar(pos)
                post = ant.getSig()
                ant.setSig(unaCelda)
                unaCelda.setSig(post)
            self.__cant += 1
        return unaCelda.getItem()

    def primerElemento(self):
        return self.__cabeza.getItem()

    def ultimoElemento(self):
        return self.__ul.getItem()

    def buscar(self, pos):
        aux = self.__cabeza
        i = 0
        while i < self.__cant and i < pos:
            aux = aux.getSig()
            i += 1
        return aux

    def recuperar(self, pos):
        if self.__cant+1 > pos > 0:
            pos -= 1
            aux = self.buscar(pos)
            return aux
        else: print('\nError posicion no valida')

    def anterior(self, pos):
        if self.__cant+1 > pos > 0:
            pos -= 2
            aux = self.buscar(pos)
            return aux
        else: print('\nError posicion no valida')

    def siguiente(self, pos):
        if self.__cant+1 > pos > 0:
            aux = self.buscar(pos)
            return aux
        else: print('\nError posicion no valida')

    def suprimir(self, pos):
        if self.__cant+1 > pos > 0:
            ant = self.anterior(pos)
            post = self.siguiente(pos)
            actual = self.recuperar(pos)
            ant.setSig(post)
            del actual
            print('Eliminado')
        else: print('\nError posicion no valida')

    def recorrer (self):
        aux = self.__cabeza
        bol = False
        while not bol:
            print(aux.getItem())
            if aux.getSig() == None:
                bol = True
            aux = aux.getSig()
            
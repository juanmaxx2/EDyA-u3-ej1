import numpy as np

class ListaSecuencialPorContenido:
    __cant = None
    __ul = None

    def __init__(self,cant):
        self.__item = np.empty(cant, dtype = int)
        self.__cant = cant
        self.__ul = 0
        self.cereo()

    def cereo (self):
        for i in range(self.__cant):
            self.__item[i] = 999999999

    def vacio(self):
        return self.__ul == 0

    def lleno(self):
        return self.__cant == self.__ul

    def shift(self,pos):
        i = self.__ul
        while i != pos-1:
            self.__item[i+1]=self.__item[i]
            i -= 1

    def insertar(self,x):
        if not self.lleno():
            i = 0
            while self.__item[i] <= x and i != self.__ul:
                i+=1
            if i == 0:
                self.__item[i] = x
            elif i == self.__ul:
                self.__item[i] = x
            else:
                self.shift(i)
                self.__item[i] = x
            self.__ul += 1
            return self.__item[i]
        else:
            print('se encuentra llena la lista')
            return 0

    def shiftAlverre(self,pos):
        i = pos
        bol = False
        while i != pos-1 and not bol:
            if i != self.__cant-1:
                self.__item[i]=self.__item[i+1]
                i += 1
            if i == self.__cant-1:
                self.__item[i] = 0
                bol = True

    def suprimir(self, pos):
        pos -= 1
        if not self.vacio():
            if 0<pos<self.__ul:
                print("\nSuprimiendo el elemento....")
                self.shiftAlverre(pos)
                print("\nEl elemento se suprimio")
                self.__ul -= 1

    def recuperar(self,pos):
        return self.__item[pos-1]

    def primerElemento(self):
        return self.__item[0]

    def ultimoElemento(self):
        return self.__item[self.__ul-1]

    def siguiente(self, pos):
        return self.__item[pos]

    def anterior(self, pos):
        pos = pos-2
        return self.__item[pos]
    
    def recorrer(self):
        for i in range(self.__ul):
            print(self.__item[i])
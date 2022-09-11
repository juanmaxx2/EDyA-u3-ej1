import numpy as np

class ListaSecuencial:
    __cant = None
    __ul = None

    def __init__(self,cant):
        self.__item = np.empty(cant, dtype = int)
        self.__cant = cant
        self.__ul = -1

    def vacio(self):
        return self.__ul == -1

    def lleno(self):
        return self.__cant == self.__ul+1
    
    def shift(self,pos):
        i = self.__ul
        while i != pos-1:
            self.__item[i+1]=self.__item[i]
            i -= 1

    def insertar(self, x, pos):
        pos -= 1
        if not self.lleno():
            if 0 <= pos <= self.__ul+1:
                if self.__ul+1 == pos:
                    self.__item[pos] = x
                    self.__ul += 1
                    return x
                elif self.__ul+1 > pos:
                    self.shift(pos)
                    self.__ul += 1
                    self.__item[pos] = x
                    return x
            else: 
                print("\nLa posicion ingresada no esta permitida")
                return 0
        else: 
            print("\nLa lista esta llena")
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
        return self.__item[self.__ul]
    
    def siguiente(self, pos):
        return self.__item[pos]
    
    def anterior(self, pos):
        pos = pos-2
        return self.__item[pos]
    
    def recorrer(self):
        for i in range(self.__ul+1):
            print(self.__item[i])
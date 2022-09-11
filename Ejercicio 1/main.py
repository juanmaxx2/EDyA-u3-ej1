from listaEncadenada import ListaEncadenada
from listaSecuencial import ListaSecuencial
from listaSecuencialPorContenido import ListaSecuencialPorContenido
from listaEncadenadaPorContenido import ListaEncadenadaPorContenido

if __name__ == "__main__":
    opcion = 0
    while opcion != '5':
        print('\n1. Ingresar una lista sencuencial')
        print('2. Ingresar una lista anidada')
        print('3. Ingresar una lista sencuencial por contenido')
        print('4. Ingresar una lista anidada por contenido')
        print('5. Salir')
        opcion = input('Ingrese la opcion a realizar:')

        if opcion == '1':
            cant = int(input("\nIngrese la cantidad de elementos de la lista:"))
            unaLista = ListaSecuencial(cant)
        elif opcion == '2':
            unaLista = ListaEncadenada()
        elif opcion == '3':
            cant = int(input("\nIngrese la cantidad de elementos de la lista:"))
            unaLista = ListaSecuencialPorContenido(cant)
        elif opcion == '4':
            unaLista = ListaEncadenadaPorContenido()

        if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4':
            i = 0
            x = int(input("\nIngrese el dato:"))

            if opcion == '1':
                while (x != 'salir') and (i < cant):
                    pos = int(input("Ingrese la posicion donde quiere insertar el elemento:"))
                    x = int(x)
                    res = unaLista.insertar(x,pos)
                    if res != 0:
                        i+=1
                    if i != cant:
                        x = input("\nIngrese el dato, 'salir' para finalizar:")
            elif opcion == '2':
                while (x != 'salir'):
                    pos = int(input("Ingrese la posicion donde quiere insertar el elemento:"))
                    x = int(x)
                    item = unaLista.Insertar(x,pos)
                    print(item)
                    x = input("\nIngrese el dato, 'salir' para finalizar:")
            elif opcion == '3':
                while (x != 'salir') and (i < cant):
                    x = int(x)
                    res = unaLista.insertar(x)
                    if res != 0:
                        i+=1
                    if i != cant:
                        x = input("\nIngrese el dato, 'salir' para finalizar:")
                    else:
                        x = 'salir'
            elif opcion == '4':
                while (x != 'salir'):
                    x = int(x)
                    item = unaLista.Insertar(x)
                    print(item)
                    x = input("\nIngrese el dato, 'salir' para finalizar:")

            print("\nEl primer elemento es: {}".format(unaLista.primerElemento()))
            print("\nEl ultimo elemento es: {}".format(unaLista.ultimoElemento()))
            x = int(input("\nIngrese el elemento a recuperar:"))

            if opcion == '1' or opcion == '3':
                print("\nEl numero recuperado es: {}".format(unaLista.recuperar(x)))
                print("\nEl anterior al numero recuperado es:{}".format(unaLista.anterior(x)))
                print("\nEl siguiente al numero recuperado es:{}".format(unaLista.siguiente(x)))
            elif opcion == '2' or opcion == '4':
                print("\nEl numero recuperado es: {}".format(unaLista.recuperar(x).getItem()))
                print("\nEl anterior al numero recuperado es:{}".format(unaLista.anterior(x).getItem()))
                print("\nEl siguiente al numero recuperado es:{}".format(unaLista.siguiente(x).getItem()))
            
            unaLista.recorrer()
            elim = int(input("\nIngrese la posicion que desea eliminar:"))
            unaLista.suprimir(elim)
            unaLista.recorrer()
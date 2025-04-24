#Implementacion de la clase nodo en la cual se guardan un dato tipo int(ubicacion de la estacion) y un dato tipo String(nombre de la estacion)
class Nodo:
    def __init__(self, siguiente=None, anterior=None, data_int=None,data_String=None):
        self.siguiente = siguiente
        self.anterior = anterior
        self.data_int = data_int
        self.data_String = data_String

#Implementacion de una lista doblemente enlazada(LDE) con los siguientes metodos para la solucion del problema
class LDE:
    def __init__(self):
        self.cabeza = None

#Metodo para agregar nodos(estacion) al principio de la lista 
    def agregarInicio(self,data_int,data_String):
        nuevo_nodo = Nodo(data_int=data_int,data_String=data_String)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

#Metodo para imprimir la lista(ruta) que se usara mas adelante
    def imprimirlista(self):
        actual = self.cabeza
        while actual:
             print(f"({actual.data_int}, {actual.data_String})", end=" - ")
             actual = actual.siguiente
        print(".")
    # Verificar si la lista esta vacia 
    def empty(self):
        if self.cabeza:
            return True
        return False
    # Contar elementos
    def count(self) -> int:
        actual = self.cabeza
        count = 0
        while actual:
            count += 1
            actual = actual.siguiente
        return count

    def search(self, data: int):
        results = []
        actual = self.cabeza
        while actual:
            if data == actual.data_int:
                while actual.data_int == data:
                    results.append(actual.data_String)
                    actual = actual.siguiente
                return results
            actual = actual.siguiente
        return "Not found"
    
    #Metodo para crear la ruta
    def ingresarEstacion(self):
        while True:
            data_int = input("Introduce la ubicacion de la estacion (o 'q' para terminar): ")
            if data_int.lower() == 'q':
                break
            data_String = input("Introduce el nombre de la estacion: ")
            if data_int.isdigit():
                self.agregarInicio(int(data_int), data_String)
            else:
                print("Por favor, introduce un número válido para la ubicacion.")    
#Metodo para ordenar la lista(ruta) utilizando el ordenamiento por mezcla
    def ordenar(self):
        self.cabeza = ordenamientoPorMezcla(self.cabeza)
  

#Aplicacion del ordenamiento por mezcla para ordenar la lista(ruta) teniendo en cuenta su valor int(la ubicacion) 
# ! O(n)
def dividirlista(head):
    slow = head
    fast = head
    while fast.siguiente and fast.siguiente.siguiente:
        slow = slow.siguiente
        fast = fast.siguiente.siguiente
    mitad = slow.siguiente
    slow.siguiente = None # * Erase connections here
    return head, mitad

def fusionar(lista1, lista2):
    if not lista1:
        return lista2
    if not lista2:
        return lista1
    if lista1.data_int < lista2.data_int:
        lista1.siguiente = fusionar(lista1.siguiente, lista2)
        lista1.siguiente.anterior = lista1
        lista1.anterior = None
        return lista1
    else:
        lista2.siguiente = fusionar(lista1, lista2.siguiente)
        lista2.siguiente.anterior = lista2
        lista2.anterior = None
        return lista2

def ordenamientoPorMezcla(head):
    if not head or not head.siguiente:
        return head
    mitadIzquierda, mitadDerecha = dividirlista(head)
    mitadIzquierda = ordenamientoPorMezcla(mitadIzquierda)
    mitadDerecha = ordenamientoPorMezcla(mitadDerecha)
    return fusionar(mitadIzquierda, mitadDerecha)

# Definicion de la Ruta
rutaBus = LDE()
print("El programa cuenta con una ruta por defecto y ofrece la opción de ingresar estaciones adicionales al usuario.")
rutaBus.ingresarEstacion()
rutaBus.agregarInicio(3,"punto a")
rutaBus.agregarInicio(7,"punto b")
rutaBus.agregarInicio(2,"punto c")
rutaBus.agregarInicio(5,"punto g")
rutaBus.agregarInicio(6,"punto y")

#Se llaman a los metodos ordenar e imprimir lista de la clase LDE y se imprime la lista(ruta) ya ordenada
rutaBus.ordenar()
print("Ruta generada:")
rutaBus.imprimirlista()
print("Número de estaciones en la ruta: ", rutaBus.count())

# Se pide el valor int(ubicacion) del nodo(parada) que el usuario desee consultar, se empieza a realizar la busqueda del nodo(estacion) 
#o los nodos(estaciones) en caso de haber mas de uno con el mismo valor int(ubicacion) y se genera una impresion

while True:
    ubi = input("Introduce la ubicacion de la estacion a buscar: ")
    if ubi.isdigit():  
        ubi = int(ubi)  
        result = rutaBus.search(ubi)
        print(result)
        break
    else:
        print("Por favor, introduce una ubicacion válida.")  

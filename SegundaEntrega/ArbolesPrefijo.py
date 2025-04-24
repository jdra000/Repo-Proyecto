class Nodo:
    def __init__(self, siguiente=None, anterior=None, data_int=None, data_String=None):
        self.siguiente = siguiente
        self.anterior = anterior
        self.data_int = data_int
        self.data_String = data_String

class LDE:
    def __init__(self):
        self.cabeza = None

    def agregarInicio(self, data_int, data_String):
        nuevo_nodo = Nodo(data_int=data_int, data_String=data_String)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def imprimirlista(self):
        actual = self.cabeza
        while actual:
            print(f"({actual.data_int}, {actual.data_String})", end=" -> ")
            actual = actual.siguiente
        print("FIN")

class NodoPrefijo:
    def __init__(self):
        self.hijos = {}
        self.final_palabra = False
        self.registros_estacion = []

class BuscadorEstaciones:
    def __init__(self):
        self.nodo_raiz = NodoPrefijo()

    def registrar_estacion(self, nombre_estacion, representacion):
        nodo_actual = self.nodo_raiz
        for caracter in nombre_estacion.lower():
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoPrefijo()
            nodo_actual = nodo_actual.hijos[caracter]
        nodo_actual.final_palabra = True
        nodo_actual.registros_estacion.append(representacion)

    def buscar_por_nombre(self, texto_parcial):
        nodo_actual = self.nodo_raiz
        for caracter in texto_parcial.lower():
            if caracter not in nodo_actual.hijos:
                return []
            nodo_actual = nodo_actual.hijos[caracter]
        sugerencias = []
        self._recorrer(nodo_actual, sugerencias)
        return sugerencias

    def _recorrer(self, nodo_inicial, lista_resultado):
        if nodo_inicial.final_palabra:
            lista_resultado.extend(nodo_inicial.registros_estacion)
        for siguiente in nodo_inicial.hijos.values():
            self._recorrer(siguiente, lista_resultado)

ruta = LDE()
buscador = BuscadorEstaciones()

def insertar_estacion(data_int, data_String):
    ruta.agregarInicio(data_int, data_String)
    buscador.registrar_estacion(data_String, f"({data_int}, {data_String})")


insertar_estacion(3, "magdanela")
insertar_estacion(1, "manguito")
insertar_estacion(2, "barranca")
insertar_estacion(5, "barrancabermeja")
insertar_estacion(4, "soledad")
insertar_estacion(6, "atlantico")

print("Ruta actual:")
ruta.imprimirlista()

while True:
    entrada = input("\nIntroduzca el nombre o parte del nombre de la estación a buscar (de lo contario introduzca 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        break

    coincidencias = buscador.buscar_por_nombre(entrada)
    if not coincidencias:
        print("No se encontraron coincidencias.")
    elif len(coincidencias) == 1:
        print(f"Se encontró una coincidencia: {coincidencias[0]}")
    else:
        print("Se encontraron varias coincidencias:")
        for i, estacion in enumerate(coincidencias, 1):
            print(f"{i}. {estacion}")
        seleccion = input("Seleccione el número de la estación que desea utilizar (): ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(coincidencias):
                print(f"Usted seleccionó: {coincidencias[seleccion - 1]}")
            else:
                print("Número fuera de rango.")
        else:
            print("Entrada no válida.")

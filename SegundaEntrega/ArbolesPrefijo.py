class NodoPrefijo:
    def __init__(self):
        self.hijos = {}
        self.final_palabra = False
        self.registros_estacion = []

class BuscadorEstaciones:
    def __init__(self):
        self.nodo_raiz = NodoPrefijo()

    def registrar_estacion(self, nombre_estacion):
        nodo_actual = self.nodo_raiz
        for caracter in nombre_estacion.lower():
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoPrefijo()
            nodo_actual = nodo_actual.hijos[caracter]
        nodo_actual.final_palabra = True
        nodo_actual.registros_estacion.append(nombre_estacion)

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
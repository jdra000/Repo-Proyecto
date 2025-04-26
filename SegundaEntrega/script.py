from bigtree import Node, print_tree
from ArbolesPrefijo import BuscadorEstaciones

class node:
    def __init__(self, data):
        self.data = data
        self.padre = None
        self.nivel = 1

Buscador = BuscadorEstaciones()
listaNodos = []
listaBigTree = []

weight = 1
tempOrder = 0
order = 1

data = input("ingrese estacion principal: ")
nodeRoot = node(data)
listaNodos.append(nodeRoot)
Buscador.registrar_estacion(nodeRoot.data)

rootBigtree= Node(nodeRoot.data) 
listaBigTree.append(rootBigtree)   

while True:
    try:
        root = listaNodos.pop(0)
        rootBigTree = listaBigTree.pop(0)
    except IndexError:
        break
    
    while True:
        data = input(f"ingrese las estaciones siguientes a {root.data} en el nivel {root.nivel+1} o q para continuar el recorrido: ")
        if data == "q":
            if tempOrder > order :
                order = tempOrder
            tempOrder = 0
            break
        else:
            nodeIns = node(data)
            nodeIns.padre = root
            bigtreeNode= Node(nodeIns.data, parent = rootBigTree)
            nodeIns.nivel = root.nivel + 1

            Buscador.registrar_estacion(nodeIns.data)

            listaNodos.append(nodeIns)
            listaBigTree.append(bigtreeNode)
            weight += 1
            tempOrder += 1

print(f"Arbol con {root.nivel} niveles")
print(f"Arbol con un peso de {weight}")
print(f"Arbol con un orden de {order}")

print_tree(rootBigtree)
buscar = int(input("Pulse 1 para entrar al buscador: "))
if buscar == 1 :


    while True:
        entrada = input("\nIntroduzca el nombre o parte del nombre de la estación a buscar (de lo contario introduzca 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break

        coincidencias = Buscador.buscar_por_nombre(entrada)
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

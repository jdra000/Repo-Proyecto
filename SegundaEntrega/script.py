class node:
    def __init__(self, data):
        self.data = data
        self.padre = None
        self.nivel = 1

nodeList = []
treeNodes = {}
weight = 1
tempOrder = 0
order = 1

data = input("ingrese estacion principal: ")
nodeRoot = node(data)
nodeList.append(nodeRoot)
treeNodes[1] = []
while True:
    try:
        root = nodeList.pop(0)
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
            nodeIns.nivel = root.nivel + 1

            nodeList.append(nodeIns)
            weight += 1
            tempOrder += 1

print(f"Arbol con {root.nivel} levels")
print(f"Arbol con un peso de {weight}")
print(f"Arbol con un orden de {order}")


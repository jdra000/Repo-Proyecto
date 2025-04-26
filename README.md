## Integrantes
* Laura Natalia Ballesteros Gualdrón 2221650
* Héctor Alirio Valdeleon Millan 2230063
* Nicol Alexa Rodriguez Alfonso 2240071
* Juan David Rey Ardila 2210080

## Primera Entrega
Debido al funcionamiento de las listas enlazadas, y lo poco eficiente que estas resultan para realizar búsquedas - debido a no tener acceso aleatorio a los elementos dentro de ella-, decidimos implementar dos scripts que solucionan el problema de ordenamiento y búsqueda dentro de una lista doblemente enlazada.

script1.py

El primer script contiene todas las implementaciones propuestas en el moodle.
Para el método de búsqueda utilizamos merge sort, y a partir de ahí, búsqueda secuencial, tanto para el método de conteo, como para el de impresión de la lista, que es lo más óptimo en este caso.
Cabe resaltar que el algoritmo de merge sort para listas enlazadas toma la forma O(logn), y el de búsqueda lineal O(n).

skip-list.py

El segundo script es un paso adelante en tiempos de ejecución y funciona bajo la estructura skip-list. Esta estructura se asemeja a la del metro de varias ciudades del mundo, y funciona por niveles, con la cabeza en la esquina superior izquierda y con valor menos infinito por defecto.

Para la implementación utilizamos 4 apuntadores por nodo, con todos los nodos en el primer nivel (nivel 0) y en los niveles superiores algunos de ellos, escogidos bajo aleatoriedad dentro del método insertar.

¿ Cómo funciona el algoritmo? 
Insertar:
1.	Buscar(x) y encontrar dónde debería estar posicionado en la lista con nivel 0.
2.	Insertar x en la lista con nivel 0 para cumplir con la invariante que nos advierte de la existencia de todos los nodos en el primer nivel.
3.	Lanzar una moneda. Mientras el resultado sea cara, promover el nodo a un nivel superior manteniendo la cabeza como extremo izquierdo en el nuevo nivel. De lo contrario, detener el procedimiento. (Este paso lo implementamos mediante la librería random de python)

Eliminar:
1.	Buscar(x) y encontrar su posición.
2.	Si x está en primer nivel. Desvincular sus apuntadores.
3.	Si x está en un nivel superior. Desvincular sus apuntadores desde arriba hasta el nivel 0 o primer nivel.
 
Buscar:
1.	Caminar la lista desde la esquina superior izquierda. Último nivel. Hasta encontrar un nodo con valor superior al que queremos buscar.
2.	Bajar de nivel.
3.	Seguir caminando hasta encontrar x o un nodo mayor que x.

Por defecto, el método de búsqueda retorna el nodo encontrado sea cual sea su nivel, sin embargo, esto no sucede cuando el nodo no se encuentra en la lista, y es ahí en donde el método insertar basa su funcionamiento, ya que si el nodo no se encuentra, el método de búsqueda bajará hasta el primer nivel o nivel 0 y devolverá la posición en donde debería estar, para luego realizar su inserción. Esto por defecto sucede en el nivel 0, puesto que si un nodo no está en un nivel superior, no estará tampoco en el nivel 0, y el método de búsqueda llegará hasta este nivel para encontrar la posición correcta.

Skip List se construye bajo aleatoriedad y aunque no es exactamente igual a un árbol binario, toma una forma parecida a un árbol. Sus métodos insertar, eliminar, y buscar, toman la forma O(logn).
![Texto alternativo](./img/1.jpg)

Recursos:

https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/resources/lecture-12-skip-lists/

https://www.osa.fu-berlin.de/bioinformatics_msc/en/exemplary_tasks/informatics_algorithms/index.html

## Segunda Entrega

Al momento de realizar el cambio en la estrucutra de datos de la primera entrega, nos dimos cuenta de lo efectivo que resultan los árboles para el manejo de las rutas, ya que cada nodo hijo hace referfencia a una parada dentro de la ruta a seguir.
Debido a esto, decidimos continuar con la temática de rutas utilizada en la primera entrega, pero esta vez permitiéndole al usuario crear la estrucutra al inicio del programa y durante este proceso calculamos el peso, nivel y grado del arbol que se está construyendo. Además, implementamos la libreria BigTree para utilizar su función de impresión para ver graficamente lo construido, y en conjunto con nuestra clase nodo, crear el mmismo.
Luego de haber implementado las funcionalidades básicas de la primera entrega, construimos un método de búesqueda mediante árboles prefijos, el cual encuentra coincidencias en base a lo ingresado en consola por el usuario.

¿Cómo funciona el código?
 1. Se solicita al usuario ingresar el nombre de los nodos nivel tras nivel.
 2. Se le muestra al usuario el árbol construido.
 3. El usuario pulsa 1 para ingresar al método adicional de búsqueda.

¿Cómo funciona el árbol prefijo (método de búsqueda)?
 1. Por cada nodo que fue creado en la funcionalidad básica, se recorre cada letra de este nodo y se crea un diccionario para cada letra, el cual tiene como valor el siguiente nodo. De esta manera, se construye una cádena de nodos que servirá para el método de coincidencias más adelante.
 2. Se recorre el árbol prefijo letra por letra de la cadena ingresada por el usuario, este recorrido finaliza en el último caracter escrito por el usuario.
 3. Una vez ubicado el último nodo, se buscan las ramas que coinciden por la cadena ingresada por el usuario. Estas coincidencias se le ofrecen al usuario con el fin de que pueda escoger la estación que busca.
 4. Luego de realizar la selección de la estación correcta, se busca su posición en el árbol inicialmente creado, con el fin de informarle al usuario cuantas estaciones debe pasar desde la estación raiz, incluyendola, para llegar a la estación deseada.
    
![Texto alternativo](./img/2.png)

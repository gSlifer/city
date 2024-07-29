TAREA 2 PARTE 1
Nicolas Caceres Plaza

---- Controles ----

WASD para movimiento en los ejes X e Y
🡩🡠🡢🡣 para el movimiento de la cámara
Q para subir en el eje Z
E para bajar en el eje Z
ESPACIO para intercambiar la cámara

LEFT CTRL para ver los polígonos sin rellenar

ESC para salir

---- Módulos ----

en libs, setup.py se encarga de crear todo lo que aparece en la escena
T2P1.py es el programa principal

las carpetas de assets y libs contienen modulos útiles para la realización del proyecto

---- Notas ----

en setup.py encontramos las funciones createPrisma1, createPrisma2 y createPrismaTriangular, las cuales nos serviran para crear 
y aplicar texturas a las primitivas necesarias de nuestra escena. 

luego, createHouse, createHouse2 y createHouse3 crearán los nodos de las casas a partir de la combinación de nodos de paredes, 
puertas, ventanas, techo y un nodo extra para cubrir una zona del techo.

createTree, createTree2 y createTree3, nos otorgan el mismo árbol pero con distintas texturas para dar algo de color al bosque,
estos están compuestos por nodos de tronco, ramas y hojas.

createField corresponderá al nodo del suelo, donde habrá un piso de pasto y las distintas calles.

por último, createScene creará la escena final, colocando las casas, arboles y el suelo en sus lugares

en T2P1 el codigo es bastante similar al utilizado en los auxiliares, algunos puntos importantes a notar son:
en controller, añadimos una variable para alternar entre los 2 tipos de cámara
en main(), además de el código típico para crear una ventana, definimos textureShaderProgram y colorShaderProgram como los shaders
creamos la escena (createScene) y definimos los parámetros de la cámara
en el loop principal, tenemos el movimiento de la camara (y sus bordes de movimiento para no salir de escena) y el cambio de tipo de camara

Por ultimo notar que el programa sufre una pequeña pérdida de frames en los primeros segundos, pero no persiste el problema de rendimiento
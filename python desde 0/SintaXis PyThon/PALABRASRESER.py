
##############_ Palabras reservadas en Pythonm _#################
##############_ Python tiene un conjunto de palabras reservadas que no podemos utilizar _##############
###############_ para nombrar variables ni funciones, _#################
###############_ ya que las reserva internamente para su funcionamiento. _###############

#Por ejemplo, no podemos llamar a una función True, y si intentamos hacerlo, 
#tendremos un SyntaxError. Esto es lógico ya que 
#Python usa internamente True para representar el tipo booleano.

#def True():
 # pass
# SyntaxError: invalid syntax
#Análogamente, no podemos llamar a una variable is ya que se trata del operador 
#de identidad.

#is = 4
# SyntaxError: invalid syntax
#Resulta lógico que no se nos permita realizar esto, ya que de ser posible,
# podríamos romper el lenguaje. Algo muy importante a tener en cuenta 
#es que palabras #
#como list no están reservadas, y esto es algo que puede generar problemas. 
#El siguiente código crea una lista usando la función estándar de Python list().

a = list("letras")
print(a)
# ['l', 'e', 't', 'r', 'a', 's']
#Sin embargo, y aunque pueda parece extraño, podemos crear una función con ese nombre.
# Al hacer esto, nos estamos cargando la función list() de Python, y por lo tanto al intentar hacer 
#la llamada anterior falla, ya que nuestra función en este caso no acepta argumentos. 
#Mucho cuidado con esto.

def list():
    print("Funcion list")

a = list("letras")
# TypeError: list() takes 0 positional arguments but 1 was given
#Pero volviendo a las palabras reservadas, 
#Python nos ofrece una forma de acceder a estas palabras programmatically, 
#es decir, a través de código. Aquí tenemos un listado con todas las palabras reservadas.

import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
#Vistas ya las palabras reservadas de Python, a continuación explicaremos 
#para que sirve cada una de ellas y las pondremos en contexto.
####### CONDICIONALES if, elif, else ########

#El uso del if y los condicionales en general son la base de cualquier lenguaje de programación.
#Son usados para alterar la línea de ejecución del programa en función de determinadas condiciones.

#En el siguiente ejemplo podemos ver su uso. De los tres bloques, 
#sólo se ejecutará uno de ellos, el cual cumpla la condición establecida 
#sobre lenguaje.

lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor

######## Bucles: while, for, break, continue #########
#El while y for permiten crear bucles que ejecutan una sección de código 
    #repetidas veces.
# Por otro lado el continue y el break permiten realizar alteraciones sobre el bucle.

#El while ejecuta su sección de código mientras se cumpla una determinada condición.

x = 0
while x < 3:
    print(x)
    x += 1

# Salida: 0, 1, 2
#El for permite iterar clases iterables, ejecutando la sección de código tantas veces como elementos tiene el iterable.

for i in range(3):
    print(i)

# Salida: 0, 1, 2
#El continue salta hasta el final del bloque, dejando sin ejecutar lo restante, 
#pero continúa en la siguiente iteración.

for i in range(3):
    if i == 1:
        continue
    print(i)

# Salida: 0, 2
#Por último, el break rompe la ejecución del bucle, saliendo del mismo.

x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1

# Salida: 0, 1, 2
#Valores: False, True, None
#False, True y None son valores que pueden ser asignados a variables, 
#siendo los dos primeros booleanos y el último algo parecido al null de otros lenguajes de programación.

#Si realizamos una comparación usando el operador relacional == se nos devolverá True o False.

x = (5 == 1)
print(x)
# Salida: False
##También podemos asignar nosotros True a una variable.

x = True
if x:
    print("Python!")
    
# Salida: Python!
#Por otro lado None se devuelve por defecto cuando una función no cuenta con un return.

def mi_funcion():
    pass

print(mi_funcion())
# Salida: None
#Operadores lógicos: and, or, not
#El and, or y not son operadores lógicos que actúan sobre valores booleanos. 
#El primero es verdadero si y solo si todos los operandos son verdaderos. 
#El segundo devuelve verdadero si al menos un elemento es verdadero. 
#Y por último, el not invierte verdadero por falso y viceversa.

print(True and False) # False
print(True or False)  # True
print(not True)       # False
#Funciones: def, return, lambda, pass, yield
#Todas ellas relacionadas con las funciones. El uso de def nos permite crear una función.

def funcion_suma(a, b):
    print("La suma es", a + b)

funcion_suma(3, 5)

# Salida: La suma es 8
#Si queremos que la función devuelva uno o varios valores, podemos usar return.

def funcion_suma(a, b):
    return a + b

suma = funcion_suma(3, 5)
print("La suma es", suma)

# Salida: La suma es 8
#El uso de lambda nos permite crear funciones lambda, 
#una especie de funciones “para vagos”. Dichas funciones no tienen un nombre per se,
#salvo asignado explícitamente.

print("La suma es", (lambda a, b: a + b)(3, 5))

# Salida: La suma es 8
#Por otro lado, podemos usar pass cuando no queramos definir la función, 
#es decir si la queremos dejar en blanco por el momento. 
#Nótese que también puede ser usado en clases, estructuras de control, etc.

def funcion_suma(a, b):
    pass
#Por último, yield está asociado a los generadores y las corrutinas, 
#un concepto un tanto avanzado pero muy interesante. 
#En el siguiente generador vemos como se generan tres valores, 
#obteniendo uno cada vez que iteramos el generador.

def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)

# Salida: 1, 2, 3
#Los generadores pueden ser usados para generar secuencias infinitas de valores, 
#sin que tengan que ser almacenados a priori, siendo creados bajo demanda. 
#Este es una utilidad muy importante trabajando con listas muy grandes, 
#cuyo almacenamiento en memoria sería muy costoso.

#Clases: class
#El uso de class nos permite crear clases. 
#Las clases son el núcleo de la programación orientada objetos, 
#y son una especie de estructura de datos que agrupa un conjunto de funciones (métodos) y variables (atributos).

class MiClase:
    def __init__(self):
        print("Creando objeto de MiClase")

objeto = MiClase()

# Salida: Creando objeto de MiClase
#Excepciones: assert, try, except, finally, raise
#Las palabras clave assert, try, except, 
#finally y raise están relacionadas con las excepciones, 
#y nos permiten tratar el qué hacer cuando las cosas no salen como esperamos. 
#El siguiente código intenta hacer un cast de cadena a entero, 
#manejando un posible error.

#Si x="10" el casteo se realiza sin problemas, 
#ya que es posible representar esa cadena como un entero. 
#Sin embargo hay que estar preparados siempre para lo peor.
#Si x="a" no se podría hacer int() y tendríamos un error. 
#Si no manejamos este error, el programa se pararía, y esto no es algo deseable. 
#El uso de try, except y finally nos permite controlar 
#dicho error y actuar en consecuencia sin que el programa se pare.
x = "10"

valor = None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error:", e)
finally:
    print("El valor es", valor)

# Salida: El valor es 10
#Variables: global, nonlocal
#El uso de global permite realizar lo siguiente, 
#y de no usarlo tendríamos un UnboundLocalError. Aunque puede resultar muy útil,
#mucho cuidado con las variables globales.

a = 0

def suma_uno():
    global a
    a = a + 1

suma_uno()
print(a)

# Salida: 1
#El uso de nonlocal es útil cuando tenemos funciones anidadas. 
#El el siguiente ejemplo podemos ver como cuando funcion_b modifica x, 
#también afecta a la x de la funcion_a, ya que la hemos declarado como nonlocal. 
#Te invitamos a que elimines el nonlocal y veas el comportamiento.

def funcion_a():
    x = 10

    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)


funcion_a()

# Salida:
# funcion_b 20
# funcion_a 20
######## Módulos: from, import ##########
#El uso de from e import nos permite importar módulos o librerías, 
#tanto estándar de Python como externas o definidas por nosotros. 
#En ejemplos como este es donde podemos ver que la sintaxis de 
#Python se asemeja bastante al lenguaje natural: de collections importa namedtuple.

from collections import namedtuple
#Pertenencia e Identidad: in, is
#El uso de in nos permite saber si un determinado elemento está en una clase iterable, devolviendo True en el caso de que sea cierto.

lista = ["a", "b", "c"]
print("a" in lista)

# Salida: True
#El uso de is nos permite saber si dos variables apuntan en realidad al mismo objeto. Por debajo se usa la función id() y es importante notar que la igualdad == no implica que is sea True.

a = [1, 2]
b = [1, 2]
c = a

print(a is b) # False
print(a is c) # True
#Eliminar variables: del
#El uso de del nos permite eliminar una variable del scope, 
#pudiendo resultar útil cuando trabajamos con variables que almacenan gran cantidad de datos. Es una manera explícita de indicar que ya no queremos una variable, pero no olvidemos que Python tiene gargabe collector.

a = 10
del a
print(a)

# Salida: NameError: name 'a' is not defined
#Context Managers: with, as
#El uso de with y as es muy utilizado a la hora de manejar ficheros, pero en realidad pertenecen a los context managers o gestores de contexto, un concepto algo avanzado.

with open('fichero.txt', 'r') as file:
    print(file.read())
######## Concurrencia: async, await ########
#El uso de async y await nos permite ejecutar procesos de manera 
#concurrente en vez de secuencial. 
#Imaginemos un proceso() que tarda 10 segundos en ejecutarse,
#ya que realiza una petición a una base de datos que lo bloquea durante ese tiempo.
#Sin esta herramienta, si quisiéramos ejecutar 3 veces el proceso 
#tardaríamos 30 segundos, ya que por defecto se ejecutan de manera secuencial,
#hasta que uno no acaba no pasamos al siguiente.

#Sin embargo, creando una función async y usando await, 
#podemos paralelizar la ejecución de los procesos, aprovechando el tiempo “muerto” 
#mientras se retorna al await. 
#En el siguiente ejemplo podemos ver como se tarda unos 10 segundos en ejecutar los 3 procesos.

import asyncio

async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(10)
    print("Acaba proceso:", id_proceso)

async def main():
    await asyncio.gather(proceso(1), proceso(2), proceso(3))

asyncio.run(main())

# Salida:
# Empieza proceso: 1
# Empieza proceso: 2
# Empieza proceso: 3
# Acaba proceso: 1
# Acaba proceso: 2
# Acaba proceso: 3
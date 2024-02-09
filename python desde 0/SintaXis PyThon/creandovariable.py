####### CREANDO VARIABLES ########

#Podemos por ejemplo asignar el mismo valor a diferentes variables con el siguiente código.

x = y = z = 10

# o también podemos asignar varios valores separados por coma.

x, y = 4, 2
x, y, z = 1, 2, 3

#nombrando variables

#El nombre no puede empezar por un número
#No se permite el uso de guiones -
#Tampoco se permite el uso de espacios.

#Se muestran unos ejemplos de nombres de variables válidos y no válidos.

# Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

# No válido
#2variable = 10
#var-iable = 10
#var iable = 10

########## DEFINICIÓN DE VARIABLES #########

#El siguiente código simplemente define tres valores a, b y c, 
#realiza unas operaciones con ellos y muestra el resultado por pantalla.

# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"

# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2

# Realizamos unas operaciones con a,b,c
d = (a + b) * c

# Definimos una variable booleana
imprimir = True

# Si imprimir, print()
if imprimir:
    print(x, d)

# Salida: El valor de (a+b)*c es 14

########## VARIABLES Y ALCANCE ###########
#Un concepto muy importante cuando definimos una variable, 
#es saber el alcance o scope que tiene. 
#En el siguiente ejemplo la variable con valor 10 tiene un alcance global y la que tiene 
#el valor 5 dentro de la función, tiene un alcance local. 
#Esto significa que cuando hacemos print(x), estamos accediendo a la variable global x y 
#no a la x definida dentro de la función.


x = 10

def funcion():
    x = 5

funcion()
print(x)

########## Uso de la función print() ##########

#Como ya hemos visto se puede usar print() para imprimir por pantalla el texto que queramos.

print("Esto es el contenido a imprimir")
#También es posible imprimir el contenido de una variable.

x = 10
print(x)
#Y separando por comas , los valores, es posible imprimir el texto y el contenido de variables.

x = 10
y = 20
print("Los valores x, y son:", x, y)
# Salida: Los valores x, y son: 10 20#


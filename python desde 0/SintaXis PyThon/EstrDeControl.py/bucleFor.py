############# Bucle for #################
#A continuación explicaremos el bucle for y sus particularidades en Python, 
#que comparado con otros lenguajes de comparación, tiene ciertas diferencias.

#El for es un tipo de bucle, parecido al while pero con ciertas diferencias. 
#La principal es que el número de iteraciones de un for esta definido de antemano, 
#mientras que en un while no. 
#La diferencia principal con respecto al while es en la condición. 
#Mientras que en el while la condición era evaluada en cada iteración para decidir 
#si volver a ejecutar o no el código, en el for no existe tal condición, 
#sino un iterable que define las veces que se ejecutará el código. 
#En el siguiente ejemplo vemos un bucle for que se ejecuta 5 veces, 
#y donde la i incrementa su valor “automáticamente” en 1 en cada iteración.

for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4
#Si has leído el capítulo del while, 
#tal vez ya empieces a ver ventajas en el uso del for. 
#Si por ejemplo, queremos tener un número que va creciendo de 0 a n, 
#hacerlo con for nos ahorra alguna línea de código, 
#porque no tenemos que escribir código para incrementar el número.

#En Python se puede iterar prácticamente todo, 
#como por ejemplo una cadena. 
#En el siguiente ejemplo vemos como la i va tomando los valores de cada letra. 
#Mas adelante explicaremos que es esto de los iterables e iteradores.

for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n
############# Iterables e iteradores ###############
#Para entender al cien por cien los bucles for,
#y como Python fue diseñado como lenguaje de programación, 
#es muy importante entender los conceptos de iterables e iteradores. 
#Empecemos con un par de definiciones:

#Los iterables son aquellos objetos que como su nombre indica pueden ser iterados, 
#lo que dicho de otra forma es, que puedan ser indexados. 
#Si piensas en un array (o una list en Python), 
#podemos indexarlo con lista[1] por ejemplo, por lo que sería un iterable.
#Los iteradores son objetos que hacen referencia a un elemento, 
#y que tienen un método next que permite hacer referencia al siguiente.
#Para saber más: Si quieres saber más sobre los iteradores te dejamos este enlace a la documentación oficial.

#Ambos son conceptos un tanto abstractos y que pueden ser complicados de entender. 
#Veamos unos ejemplos. Como hemos comentado, 
#los iterables son objetos que pueden ser iterados o accedidos con un índice. 
#Algunos ejemplos de iterables en Python son las listas, tuplas, 
#cadenas o diccionarios. 
#Sabiendo esto, lo primero que tenemos que tener claro es que en un for, 
#lo que va después del in deberá ser siempre un iterable.

#for <variable> in <iterable>:
#    <Código>
#Tiene bastante sentido, porque si queremos iterar una variable, 
#esta variable debe ser iterable, todo muy lógico. 
#Pero llegados a este punto, tal vez de preguntes ¿pero cómo se yo si algo es iterable o no?. 
#Bien fácil, con la siguiente función isinstance() podemos saberlo. 
#No te preocupes si no entiendes muy bien lo que estamos haciendo, 
#fíjate solo en el resultado, True significa que es iterable y False que no lo es.

from collections import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #False
#Por lo tanto las listas y las cadenas son iterables, 
#pero numero, que es un entero no lo es. 
#Es por eso por lo que no podemos hacer lo siguiente, ya que daría un error. 
#De hecho el error sería TypeError: int' object is not iterable.

numero = 10
#for i in numero:
#    print(i)
#Una vez entendidos los iterables, veamos los iteradores. 
#Para entender los iteradores, es importante conocer la función iter() en Python. 
#Dicha función puede ser llamada sobre un objeto que sea iterable,
#y nos devolverá un iterador como se ve en el siguiente ejemplo.

lista = [5, 6, 3, 2]
it = iter(lista)
print(it)       #<list_iterator object at 0x106243828>
print(type(it)) #<class 'list_iterator'>
#Vemos que al imprimir it es un iterador, de la clase list_iterator. 
#Esta variable iteradora, 
#hace referencia a la lista original y 
#nos permite acceder a sus elementos con la función next(). 
#Cada vez que llamamos a next() sobre it, 
#nos devuelve el siguiente elemento de la lista original. 
#Por lo tanto, si queremos acceder al elemento 4, 
#tendremos que llamar 4 veces a next(). 
#Nótese que el iterador empieza apuntando fuera de la lista, 
#y no hace referencia al primer elemento hasta que no se llama a next() 
#por primera vez.

lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
#     [5, 6, 3, 2]
#      ^
#      |
#     it
print(next(it))
#     [5, 6, 3, 2]
#         ^
#         |
#        it
print(next(it))
#     [5, 6, 3, 2]
#            ^
#            |
#           it
#Para saber mas: Existen otros iteradores para diferentes clases:

#str_iterator para cadenas
#list_iterator para sets.
#tuple_iterator para tuplas.
#set_iterator para sets.
#dict_keyiterator para diccionarios.
#Dado que el iterador hace referencia a nuestra lista, si llamamos más veces a next() 
#que la longitud de la lista, se nos devolverá un error StopIteration. 
#Lamentablemente no existe ninguna opción de volver al elemento anterior.

lista = [5, 6]
it = iter(lista)
print(next(it))
print(next(it))
#print(next(it)) # Error! StopIteration
#Es perfectamente posible tener diferentes iteradores para la misma lista, 
#y serán totalmente independientes. Tan solo dependerán de la lista, 
#como es evidente, pero no entre ellos.

lista = [5, 6, 7]
it1 = iter(lista)
it2 = iter(lista)
print(next(it1)) #5
print(next(it1)) #6
print(next(it1)) #7
print(next(it2)) #5
#For anidados
#Es posible anidar los for, es decir, meter uno dentro de otro. 
#Esto puede ser muy útil si queremos iterar algún objeto que en cada elemento, 
#tiene a su vez otra clase iterable. Podemos tener por ejemplo, una lista de listas, 
#una especie de matriz.

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
#Si iteramos usando sólo un for, estaremos realmente accediendo a la segunda lista, 
#pero no a los elementos individuales.

for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]
#Si queremos acceder a cada elemento individualmente, podemos anidar dos for. 
#Uno de ellos se encargará de iterar las columnas y el otro las filas.

for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3
#Ejemplos for
#Iterando cadena al revés. 
#Haciendo uso de [::-1] se puede iterar la lista desde el último al primer elemento.

texto = "Python"
for i in texto[::-1]:
    print(i) #n,o,h,t,y,P
#Itera la cadena saltándose elementos. Con [::2] vamos tomando un elemento si
#y otro no.

texto = "Python"
for i in texto[::2]:
    print(i) #P,t,o
#Un ejemplo de for usado con comprehensions lists.

print(sum(i for i in range(10)))

# Salida: 45
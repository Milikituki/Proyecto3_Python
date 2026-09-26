# Proyecto2_KatasJS

### EJERCICIO 1:

Inicializamos el diccionario vacío, luego con un for recorremos la cadena de texto y, si no está vacía, vamos sumando 1 para dar después la cantidad de veces que la letra se repite.

### EJERCICIO 2:

Aquí aplicamos la función lambda en cada elemento con map() y lo convertimos en una lista

### EJERCICIO 3:

Hacemos que la función devuelva las palabras que contienen el objetivo mediante un for que recorre la lista original y luego filtra con un if.

### EJERCICIO 4:

Aquí map() recorre las dos listas en paralelo y va restando al primer elemento el segundo sucesivamente.

### EJERCICIO 5:

Primero calculamos la media de la lista para después filtrar el estado según la media anterior y devolvemos los valores como una tupla.

### EJERCICIO 6:

Aquí usamos la recursividad planteando primero el caso base y luego haciendo la llamada a la función multiplicando n por el factorial de n-1

### EJERCICIO 7:

map() recorre las lista y str va convirtiendo los elementos en String para que devuelva la lista con ese tipo.

### EJERCICIO 8:

Primero tenemos que pedir los números con input para luego realizar la división. Luego, tratamos las posibles excepciones para que muestren mensajes dependiendo del caso que la haya lanzado.

### EJERCICIO 9:

En este ejercicio he usado filter para poder filtrar la lista de mascotas y poder excluir con el "not in" los que se encuentran en la lista de "forbidden pets"

### EJERCICIO 10:

Primero definimos la excepción personalizada que saltará cuando la lista esté vacía. Luego, comprobamos si la lista está vacía con un if y finalizamos tratando la excepción en el bloquee "except".

### EJERCICIO 11:

Dentro de la variable "age" guardamos el dato que nos da el usuario y luego lo filtramos con un if. En caso de que la edad no esté comprendida en el rango indicado, salta la excepción que hemos manejado en el bloque.

### EJERCICIO 12:

Primero tenemos que dividir la la frase por palabras usando split() y luego aplicamos len() usando map() para que que a la vez que va recorriendo, determine la longitud.

### EJERCICIO 13:

Eliminamos los duplicados mediante un set y luego devolvemos una tupla por cada letra

### EJERCICIO 14:

Filtramos las palabras que empiezan con la letra que se ha indicado con filter primero y luego con "startswith" y devolvemos una lista con el resultado.

### EJERCICIO 15:

Usamos lambda con un for que va recorriendo la lista de números y a la vez va sumando 3 a dichos elementos.

### EJERCICIO 16:

Primero se divide la cadena de texto con split() y luego con filter() filtramos las palabras que tengan longitud (len) mayor a la indicada por la variable n.

### EJERCICIO 17:

Acumulamos cada número multiplicando por 10 con acc, que va guardando el resultado acumulado de las operación anterior, y luego sumamos el siguiente para obtener el número correspondiente

### EJERCICIO 18:

Usamos filter() para filtrar los estudiantes con una calificación mayor a la indicada atacando a la clave del diccionario.

### EJERCICIO 19:

Aquí usamos lambda: numbers con filter() para filtrar los números de la lista mediante la condición (lambda: number) que comprueba si el resto de dividirlo entre 2 es 0. Si da true, se queda y si es false, se descarta.

### EJERCICIO 21:

Para conseguir que el número se eleve al cubo tenemos que usar el operador de potencia "**".

### EJERCICIO 22:

Aquí tenemos que multiplicar los elementos de manera acumulativa (acc * number) y luego con reduce() lo reducimos a un único valor final.

### EJERCICIO 23:

Volvemos a usar acc para poder ir concatenando acumulativamente la secuencia de palabras que tenemos en la lista-

### EJERCICIO 24:

También usamos acc para poder restar de manera acumulativa. Es prácticamente el mismo ejercicio que el anterior pero con diferente operador aritmético.

### EJERCICIO 25:

En este caso podemos usar la función len() para poder obtener el número de caracteres en la cadena de texto dada.

### EJERCICIO 26:

Aquí sólo tenemos que indicar el operador correcto (%) para poder obtener el resto de la división.

### EJERCICIO 27:

Calculamos la media mediante la función sum() que suma los elementos de la lista y luego dividiendo por la longitud de la lista con len().

### EJERCICIO 28:

Primero creamos una variable que guarde un conjunto para ir guardando los registros de los elementos ya vistos. Luego con el for recorremos cada elemento y con el if filtramos si el elemento ya estaba en el set, en cuyo caso es el primer duplicado. Si no hay ningún duplicado, devolveremos None.

### EJERCICIO 29:

Para esto tenemos que usar str() que convierte los valores a texto. Luego filtramos con un if si la longitud de ese texto cumple la condición y en caso de que así sea, será lo que retorne la función. En caso contrario, sustituimos todos los caracteres con # menos los 4 últimos, usando len() para calcular la longitud del conjunto de caracteres restándole los 4 que no queremos que se enmascaren y luego haciendo un slice desde la última posición -4.

### EJERCICIO 30:

Primero tenemos que ordenar las palabras ambas palabras con sorted() que descompone la palabra en letras y las devuelve ordenadas alfabéticamente en una lista. Luego comparamos ambas listas para determinar si son idénticas, en cuyo caso devolverá true.

### EJERCICIO 31:

En este ejercicio primero creamos una excepción personalizada que hereda de la clase Exception. El siguiente paso es pedir la lista de nombres al usuario mediante input y separamos esos nombres mediante la coma "," con split(). Despues tenemos que recorrer la lista aplicando strip() a cada nombre para eliminar los espacios que pueda haber al principio y al final. También lo usaremos en input con el mismo objetivo.

Finalmente nos queda comprobar con el if si el nombre está presente o no en la lista y, si no lo está lanza la excepción.

### EJERCICIO 32:

Recorremos la lista de empleados actual con el for y comprobamos si coincide con el nombre que se está buscando mediante un if que accede al valor de la clave "nombre". Luego devolvemos el valor asociado a la clave "puesto" en caso de que haya coincidencia. En caso contrario devolvemos el mensaje especificado.

### EJERCICIO 33:

Aquí definimos la función que va a emparejar los elementos de las dos listas índice por índice con zip(). Por otro lado, iteramos sobre esas parejas y "desempaquetamos" cada dupla en dos variables ("x" e "y"), sumando los dos valores y guardando el resultado en una lista nueva.

### EJERCICIO 34:

En este ejercicio primero creamos el constructor de la clase, inicializando el árbol con 1 tronco y una lista vacía para las ramas. Luego, con el método crecer_tronco() sumamos 1 a la longitud del tronco y con nueva_rama añadimos una rama a la lista con una longitud inicial de uno con append(1). Por otro lado, incrementamos en 1 la longitud de todas las ramas de la lista. Con quitar_rama() comprobamos si el índice "position" es válido dentro del rango de la lista y, si lo es, elimina la rama en esa posición. Finalmente, retornamos un diccionario con el estado del árbol (valor de tronco, numero de ramas y la lista completa con los tamaños de cada rama)

### EJERCICIO 35:

Mediante el constructor de la clase inicializamos los atributos del usuario. Con retirar_dinero() evaluamos si la cantidad solicitada supera el saldo disponible, en cuyo caso mandamos un mensaje de error. Si el saldo es suficiente, se descuenta del balance. Para sumar el importe que se especifique al saldo de la cuenta usamos agregar_dinero().

### EJERCICIO 36:

La primera función cuenta cuántas veces se repite cada palabra, dividiendo el texto por espacios con split(). Recorre cada palabra con el formato y luego con .get() lleva el conteo y lo almacena en el diccionario. Si la palabra no existe, devuelve 0 por defecto y en caso contrario, suma 1.
Después usamos replace() para sustituir todas las palabras originales por la palabra elegida.
La siguiente función también usa replace() en el mismo sentido sólo que aquí filtramos para quedarnos sólo con las palabras que sean diferentes a la que se quiere eliminar. Devolvemos esas palabras unidas con join() y le concatenamos un espacio.
procesar_texto() actúa como menú con el que filtramos mediante condiciones para poder "desencadenar" cada función. Devolvemos un error en caso de que no se seleccione ninguna opción válida, es decir, que no se especifique ninguna de las funciones añadidas.

### EJERCICIO 37:

Pedimos al usuario mediante input que introduzca una hora y mediante un bloque if filtramos las opciones con operadores de comparación.

### EJERCICIO 38:

Mismo procedimiento que el ejercicio anterior cambiando los strings devueltos.

### EJERCICIO 39:

En este caso tenemos que determinar primero el tipo de figura de la que se trata y por cada una de ella devolvemos la ecuación matemática que le corresponda.
Si es un rectángulo, se espera que sean dos valores. Si es un círculo, se extrae el primer elemento de la colección mediante "data[0]", luego calculamos el área con la fórmula adecuada. Por último, si es un triángulo, también necesitaremos dos valores pero en este caso retornamos la mitad del producto.
En caso de que no se especifique ninguna figura válida, devolvemos un mensaje de error.

### EJERCICIO 40:

Pedirmos el precio mediante input y hacemos lo mismo para el cupón pero lo transformamos a minúsculas para facilitar la comparación posterior. Inicializamos la variable con el valor del precio original.
Analizamos los diferentes escenarios con if, de manera que se solicita el valor del cupón en el primer caso y se evalúan otra vez las condiciones. En caso de que el valor sea 0 o negativo, mostramos mensaje y no se modifica el valor de la variable del precio final. En caso de que el cupón cubra todo el precio o más, se fija dicho precio y lanzamos mensaje de que el cupón es válido. Si es un valor intermedio, restamos el cupón al total.
En caso de que señalemos que no hay cupón, lanzamos mensaje de que no se puede aplicar el descuento y para cualquier otra respuesta: "opción no válida".

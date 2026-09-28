from functools import reduce
""" 
1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados. 
"""

def count_letter_frequencies(text):
    frequencies = {}
    for letter in text.lower():
        if letter != "":
            frequencies[letter] = frequencies.get(letter, 0) + 1

    return frequencies

text = "Hola mundo"
print(count_letter_frequencies(text))

"""
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
"""

def double_values(numbers):
    return list(map(lambda a: a * 2, numbers))

numbers = [1, 2, 3, 4, 5]
print(double_values(numbers))

"""
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
"""

def find_words(words, target_word):
    return [word for word in words if target_word in word]

words = ["python", "programming", "code", "typing"]
target_word = "python"
print(find_words(words, target_word))

"""
4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
"""

def calculate_difference(list1, list2):
    return list(map(lambda a, b: a - b, list1, list2))


list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
print(calculate_difference(list1, list2))

"""
5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
"""

def calculate_average(numbers, nota_aprobado=5):
    average = sum(numbers) / len(numbers)
    status = "aprobado" if average >= nota_aprobado else "suspenso"
    return (average, status)


numbers = [4, 6, 5, 7, 3]
print(calculate_average(numbers))

"""
6. Escribe una función que calcule el factorial de un número de manera recursiva.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

"""
7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""

def tuples_to_strings(tuples_list):
    return list(map(str, tuples_list))


tuples_list = [(1, 2), (3, 4), (5, 6)]
print(tuples_to_strings(tuples_list))

"""
8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
"""

def divide_numbers():
    try:
        number1 = float(input("Introduce el primer número: "))
        number2 = float(input("Introduce el segundo número: "))
        result = number1 / number2
    except ValueError:
        print("Error: debes introducir un número")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
    else:
        print(f"Resultado: {result}")

divide_numbers()

"""
9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
"""

def filter_allowed_pets(pets):
    forbidden_pets = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda pet: pet not in forbidden_pets, pets))


pets = ["Perro", "Gato", "Mapache", "Tigre", "Conejo", "Cocodrilo"]
print(filter_allowed_pets(pets))

"""
10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
"""

class EmptyListError(Exception):
    pass


def calculate_average(numbers):
    if not numbers:
        raise EmptyListError("La lista está vacía")
    return sum(numbers) / len(numbers)

try:
    numbers = [5, 3, 9, 0]
    print(calculate_average(numbers))
except EmptyListError as e:
    print(f"Error: {e}")

"""
11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""

def request_age():
    try:
        age = int(input("Introduce tu edad: "))
        if age < 0 or age > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Tu edad es {age}.")

request_age()

"""
12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
"""

def get_word_lengths(sentence):
    words = sentence.split()
    return list(map(len, words))

sentence = "Father, why have you forsaken me?"
print(get_word_lengths(sentence))

"""
13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
"""

def letters_to_cases(characters):
    unique_letters = set(characters)
    return list(map(lambda letter: (letter.upper(), letter.lower()), unique_letters))


characters = "asdf"
print(letters_to_cases(characters))

"""
14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
"""

def filter_words(words, letter):
    return list(filter(lambda word: word.startswith(letter), words))


words = ["perro", "gato", "pato", "conejo", "pez"]
letter = "p"
print(filter_words(words, letter))

"""
15. Crea una función lambda que sume 3 a cada número de una lista dada.
"""

add_three = lambda numbers: [number + 3 for number in numbers]

numbers = [1, 2, 3, 4, 5]
print(add_three(numbers))

"""
16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
"""

def filter_longer_words(text, n):
    words = text.split()
    return list(filter(lambda word: len(word) > n, words))


text = "Father, why have you forsaken me?"
n = 4
print(filter_longer_words(text, n))

"""
17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
"""

def digits_to_number(digits):
    return reduce(lambda acc, digit: acc * 10 + digit, digits)

digits = [5, 7, 2]
print(digits_to_number(digits))

"""
18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
"""

def filter_students(students):
    return list(filter(lambda student: student["calificacion"] >= 90, students))


students = [
    {"nombre": "Miriam", "edad": 32, "calificacion": 95},
    {"nombre": "Belén", "edad": 35, "calificacion": 85},
    {"nombre": "María", "edad": 29, "calificacion": 90},
    {"nombre": "Adriana", "edad": 31, "calificacion": 70},
]

top_students = filter_students(students)
print(top_students)

"""
19. Crea una función lambda que filtre los números impares de una lista dada.
"""

filter_odd_numbers = lambda numbers: list(filter(lambda number: number % 2 != 0, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_odd_numbers(numbers))

"""
20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
"""

def filter_ints(elements):
    return list(filter(lambda element: isinstance(element, int), elements))

elements = [1, "father", 2, "why", 3, 4, "forsaken"]
print(filter_ints(elements))

"""
21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
"""

cube = lambda number: number ** 3
number = 4
print(cube(number))

"""
22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
"""

def calculate_product(numbers):
    return reduce(lambda acc, number: acc * number, numbers)

numbers = [1, 2, 3, 4, 5]
print(calculate_product(numbers))

"""
23. Concatena una lista de palabras. Usa la función reduce().
"""

def concatenate_words(words):
    return reduce(lambda acc, word: acc + word, words)

words = ["why", " ", "have", " ", "you", " ", "forsaken", "me"]
print(concatenate_words(words))

"""
24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""

def calculate_total_difference(numbers):
    return reduce(lambda acc, number: acc - number, numbers)

numbers = [100, 20, 30, 10]
print(calculate_total_difference(numbers))

"""
25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

def count_characters(text):
    return len(text)


text = "Father, why have you forsaken me?"
print(count_characters(text))

"""
26. Crea una función lambda que calcule el resto de la división entre dos números dados."""

calculate_resto = lambda a, b: a % b

a = 17
b = 5
print(calculate_resto(a, b))

"""
27. Crea una función que calcule el promedio de una lista de números.
"""

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


numbers = [4, 8, 15, 16, 23, 42]
print(calculate_average(numbers))

"""
28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""

def find_first_duplicate(elements):
    seen = set()
    for element in elements:
        if element in seen:
            return element
        seen.add(element)
    return None

elements = [3, 5, 7, 2, 5, 8, 3]
print(find_first_duplicate(elements))

"""
29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
"""

def mask_string(value):
    text = str(value)
    if len(text) <= 4:
        return text
    return "#" * (len(text) - 4) + text[-4:]


value = 665475376
print(mask_string(value))

"""
30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
"""

def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


word1 = "amor"
word2 = "roma"
print(are_anagrams(word1, word2))

"""
31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
"""

class NameNotFoundError(Exception):
    pass


def search_name():
    names = input("Introduce una lista de nombres separados por comas: ").split(",")
    names = [name.strip() for name in names]
    search = input("Introduce el nombre a buscar: ").strip()

    try:
        if search not in names:
            raise NameNotFoundError(f"El nombre '{search}' no está en la lista")
        print(f"El nombre '{search}' está en la lista")
    except NameNotFoundError as e:
        print(f"Error: {e}")


search_name()

"""
32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""

def find_employee_position(full_name, employees):
    for employee in employees:
        if employee["nombre"] == full_name:
            return employee["puesto"]
    return "La persona no trabaja aquí."


employees = [
    {"nombre": "Miriam Fernández", "puesto": "Desarrolladora"},
    {"nombre": "Miquel Amengual", "puesto": "Diseñador"},
    {"nombre": "Pau AF", "puesto": "Gerente"},
]

full_name = "Pau AF"
print(find_employee_position(employees=employees, full_name=full_name))

"""
33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""

add_lists = lambda list1, list2: [x + y for x, y in zip(list1, list2)]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(add_lists(list1, list2))

""" 
34. Crea la clase Arbol. Define un árbol genérico con un tronco y ramas como atributos.Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
Implementar el método quitar_rama para eliminar una rama en una posición específica.
Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
"""

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [length + 1 for length in self.ramas]

    def quitar_rama(self, position):
        if 0 <= position < len(self.ramas):
            del self.ramas[position]

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas,
        }

""" Caso de uso:
    a. Crear un árbol.
    b. Hacer crecer el tronco una unidad.
    c. Añadir una nueva rama.
    d. Hacer crecer todas las ramas una unidad.
    e. Añadir dos nuevas ramas.
    f. Retirar la rama situada en la posición 2.
    g. Obtener información sobre el árbol.
 """

tree = Arbol()
tree.crecer_tronco()
tree.nueva_rama()
tree.crecer_ramas()
tree.nueva_rama()
tree.nueva_rama()
tree.quitar_rama(2)

print(tree.info_arbol())

"""
35. Crea la clase UsuarioBanco
Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
Código a seguir:
Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
Implementar agregar_dinero para aumentar el saldo del usuario.
"""

class UsuarioBanco:
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def retirar_dinero(self, amount):
        if amount > self.balance:
            raise ValueError(f"No hay suficiente saldo para retirar {amount} de {self.name}.")
        self.balance -= amount

    def transferir_dinero(self, other_user, amount):
        try:
            other_user.retirar_dinero(amount)
            self.agregar_dinero(amount)
        except ValueError as e:
            raise ValueError(f"Error al transferir dinero: {e}")

    def agregar_dinero(self, amount):
        self.balance += amount

"""
Caso de uso:
        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
        b. Agregar 20 unidades al saldo de Bob.
        c. Transferir 80 unidades de Bob a Alicia.
        d. Retirar 50 unidades del saldo de Alicia.
"""

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
alicia.transferir_dinero(bob, 80)
alicia.retirar_dinero(50)

print(f"Saldo de {alicia.name}: {alicia.balance}")
print(f"Saldo de {bob.name}: {bob.balance}")

"""
36. Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
Código a seguir:
Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
"""

def count_words(text):
    words = text.split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def replace_words(text, original_word, new_word):
    return text.replace(original_word, new_word)


def remove_word(text, word):
    words = text.split()
    words = [w for w in words if w != word]
    return " ".join(words)


def procesar_texto(text, option, *args):
    if option == "contar":
        return count_words(text)
    elif option == "reemplazar":
        original_word, new_word = args
        return replace_words(text, original_word, new_word)
    elif option == "eliminar":
        word = args[0]
        return remove_word(text, word)
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

"""
Caso de uso:
Verificar el funcionamiento completo de procesar_texto.
"""

text = "father, why have you forsaken me?"

print(procesar_texto(text, "contar"))
print(procesar_texto(text, "reemplazar", "father", "My lord"))
print(procesar_texto(text, "eliminar", "you"))

"""
37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
"""

hour = int(input("Introduce la hora (0-23): "))

if hour < 0 or hour > 23:
    print("Hora no válida")
elif 6 <= hour <= 12:
    print("Es de día")
elif 13 <= hour <= 20:
    print("Es de tarde")
else:
    print("Es de noche")

"""
38. Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
Reglas:
        0 - 69: insuficiente
        70 - 79: bien
        80 - 89: muy bien
        90 - 100: excelente
"""

nota = int(input("Introduce la calificación (0-100): "))

if nota < 0 or nota > 100:
    print("Calificación no válida")
elif nota <= 69:
    print("Insuficiente")
elif nota <= 79:
    print("Bien")
elif nota <= 89:
    print("Muy bien")
else:
    print("Excelente")

"""
39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
"""

def calculate_area(shape, data):
    if shape == "rectangulo":
        base, height = data
        return base * height
    elif shape == "circulo":
        radius = data[0]
        return math.pi * radius ** 2
    elif shape == "triangulo":
        base, height = data
        return base * height / 2
    else:
        return "Figura no válida"

print(calculate_area("rectangulo", (4, 5)))
print(calculate_area("circulo", (3,)))
print(calculate_area("triangulo", (6, 4)))

"""
40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
"""

price = float(input("Introduce el precio original del artículo: "))
has_coupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()

final_price = price

if has_coupon == "sí" or has_coupon == "si":
    coupon = float(input("Introduce el valor del cupón: "))
    if coupon <= 0:
        print("Cupón no válido")
    elif coupon >= price:
        print("Cupón validado")
        final_price = 0
    else:
        final_price = price - coupon
elif has_coupon == "no":
    print("No es posible aplicar el descuento")
else:
    print("Opción no válida")

print("Precio final de la compra:", final_price, "€")
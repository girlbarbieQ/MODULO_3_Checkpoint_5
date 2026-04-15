# PYTHON DOCUMENTATION
## 🔹 ¿Qué es un condicional?
Un condicional es una estructura que permite que un programa tome decisiones. Es decir, ejecuta una parte del código únicamente cuando se cumple una condición. En Python se utilizan las palabras clave if, elif y else.

👉 Son fundamentales porque permiten que el programa se adapte a diferentes situaciones en lugar de ejecutar siempre las mismas instrucciones.

### 💻 Ejemplo
```python
edad = 20

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')
```

En este caso, el programa evalua si la edad es mayor o igual a 18 años.
- Si se cumple la condición --> muestra 'Eres mayor de edad'
- Si no se cumple --> muestra 'Eres menor de edad'

#### 🌎 Ejemplos en la vida real

##### Log in de una app
- Si la contraseña es correcta --> Entras
- Si la contraseña es incorrecta --> Error

##### Tienda Online
- Si hay stock --> puedes comprar
- Si no hay stock --> 'Agotado'

##### Juego
- Si tienes 0 vidas --> Game Over
- Si no --> el juego continua


## 🔹 ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?
Los bucles sirven para repetir acciones automáticamente sin tener que escribir el mismo código muchas veces.
Son utiles porque permiten automatizar tareas repetitivas, como recorrer listas o procesar datos.

### 🔁 Tipos de bucles
#### Bucle for
Se utilizan para recorrer elementos como listas, rangos u otras colecciones de datos.

##### 💻 Ejemplo

```python
for i in range(5):
    print(i)
```

En este caso, el programa imprime numeros del 0 al 4.

#### Bucle while
Se ejecuta mientras una condición sea verdadera.

##### 💻 Ejemplo

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1
```

En este caso, el programa repite el bloque de código hasta que el contador deja de cumplir la condición.


## 🔹 ¿Qué es una lista por comprensión en Python?
Una lista por comprensión es una forma corta y eficiente de crear listas. Permite generar listas en una sola línea, en lugar de usar varias líneas con un bucle for.
Se utiliza principalmente para hacer el código más limpio, más rápido de escribir y más fácil de leer.

👉 Es muy útil cuando quieres crear una lista a partir de otra o generar datos de forma rápida.

### 💻 Ejemplo

```python
numbers = [x for x in range (5)]
```
En este caso, el programa crea una lista de números del 0 al 4.
 
### 💻 Ejemplo

```python
pares = [x for x in range (10) if x % 2 == 0]
```
En este caso, el programa crea un lista solo con los números pares del 0 al 9.


## 🔹 ¿Qué es un argumento en Python?
Un argumento en Python es el valor que se le pasa a una función para que pueda trabajar con él. Cuando defines una función, puedes indicar qué datos necesita. Esos datos se reciben como argumentos cuando llamas a la función.
En otras palabras, los argumentos son la información que le das a una función para que haga algo.

### 💻 Ejemplo

```python
def greeting(name):
    print('Hi', name)

greeting('Bárbara')
```

En este caso, "Bárbara" es el argumento que se le pasa a la función greeting. La función utiliza ese argumento para mostrar el mensaje.

👉 Los argumentos son importantes porque permiten que las funciones sean dinámicas y reutilizables. Es decir, la misma función puede usarse con diferentes valores.

#### 🌎 Ejemplos de la vida real
- Si usamos greeting('Ana') --> Hi, Ana
- Si usamos greeting('Carlos') --> Hi, Carlos

La función es la misma pero cambia el argumento.

👉 Esto permite reutilizar la misma función con diferentes datos sin tener que crear una función nueva cada vez.


## 🔹 ¿Qué es una función Lambda en Python?
Una función lambda es una forma corta y rápida de crear funciones en Python. Se utiliza cuando necesitas una función sencilla y no quieres definirla con la palabra clave def.
A diferencia de las funciones normales, las funciones lambda se escriben en una sola línea y no tienen nombre (aunque se pueden guardar en una variable).

👉 Son útiles para operaciones simples y rápidas.

### 💻 Ejemplo

```python
suma = lambda a, b: a + b

print(suma(2, 3))
```

En este caso, la función lambda recibe dos valores (a y b) y devuelve la suma. Resultado (5).

#### 🔁 Comparación con una función normal
##### Función normal

```python
def suma(a, b):
    return a + b
```
##### Función lambda

```python
suma = lambda a, b: a + b
```

Ambas hacen lo mismo, pero la función lambda es más corta.

👉 Esto permite escribir menos código y hacer el programa más compacto.


## 🔹 ¿Qué es un paquete pip?
Un paquete pip es una herramienta que se utiliza en Python para instalar, gestionar y eliminar librerías externas.

Las librerías son conjuntos de código ya creados que otros programadores han desarrollado y que puedes usar para añadir nuevas funcionalidades a tus proyectos sin tener que programarlo todo desde cero.

Gracias a pip, puedes ampliar fácilmente lo que Python puede hacer.

### 💻 Ejemplo

```bash
pip install numpy
```
Este comando instala la librería numpy, que se utiliza para trabajar con números, cálculos matemáticos y datos.

#### 🌎 Ejemplos comunes
Algunas librerías que se pueden instalar con pip:
- numpy --> para cálculos matemáticos
- requests --> para trabajar con datos de internet
- flask --> para crear aplicaciónes web

pip es importante porque permite reutilizar código ya existente en lugar de tener que crear todo desde cero.

👉 Esto ahorra tiempo y facilita el desarrollo de proyectos más complejos.

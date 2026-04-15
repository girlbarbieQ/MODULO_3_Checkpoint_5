# PYTHON DOCUMENTATION
## 🔹 ¿Qué es un condicional?

Un condicional es una estructura de control que permite que un programa tome decisiones durante su ejecución. En lugar de ejecutar todas las instrucciones de forma secuencial, el programa evalúa una condición y decide qué bloque de código ejecutar en función del resultado.

En Python, los condicionales se construyen utilizando las palabras clave if, elif y else.

👉 Su función principal es controlar el flujo del programa, permitiendo que este se adapte a diferentes situaciones según los datos que recibe.

👉 Los condicionales son esenciales porque hacen que los programas sean dinámicos, es decir, capaces de reaccionar de forma distinta dependiendo del contexto.

👉 Sin condicionales, un programa ejecutaría siempre las mismas instrucciones, sin importar los datos de entrada, lo que limitaría enormemente su utilidad.

### 💻 Ejemplo
```python
age = 20

if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```
#### 📌 Explicación:
El programa evalúa si la variable age cumple la condición (>= 18).
- Si la condición es verdadera --> ejecuta el primer bloque
- Si es falsa --> ejecuta el bloque alternativo

👉 Este tipo de lógica se basa en valores booleanos (True o False)

##### 🧠 Conceptos clave
- Condición: expresión que se evalúa como verdadera o falsa
- Bloque de código: conjunto de instrucciones que se ejecutan si se cumple la condición
- Flujo del programa: orden en el que se ejecuta el código

###### 🌎 Ejemplos en la vida real
Los condicionales están presentes en casi cualquier aplicación real:

🔐 Login: validar usuario y contraseña
- Si la contraseña es correcta --> Entras
- Si la contraseña es incorrecta --> Error

🛒 Ecommerce: comprobar stock antes de comprar
- Si hay stock --> puedes comprar
- Si no hay stock --> 'Agotado'

🎮 Videojuegos: gestionar vidas, niveles o puntuaciones
- Si tienes 0 vidas --> Game Over
- Si no --> el juego continua

👉 En todos estos casos, el programa toma decisiones en tiempo real.





## 🔹 ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los bucles (loops) son estructuras que permiten repetir un bloque de código varias veces sin necesidad de escribirlo repetidamente.

👉 Se utilizan para automatizar tareas repetitivas, lo que hace que el código sea más eficiente y fácil de mantener.

👉 Son fundamentales cuando trabajas con colecciones de datos como listas, diccionarios o rangos.


### 🔁 Tipos de bucles
- Bucle for
  
Se utiliza para iterar sobre una secuencia (lista, rango, string, etc.).
👉 Es ideal cuando sabes cuántas veces quieres repetir una acción o cuando recorres una colección.

#### 💻 Ejemplo
```python
for i in range(5):
    print(i)
```

##### 📌 Explicación:
El bucle for recorre un rango de números, en este caso del 0 al 4.
En cada vuelta, la variable i toma un valor distinto y se ejecuta el print.
Esto permite repetir una acción varias veces sin tener que escribir el código muchas veces.

- Bucle while
  
Se ejecuta mientras una condición sea verdadera.

👉 Es útil cuando no sabes exactamente cuántas veces se repetirá el proceso.

#### 💻 Ejemplo
```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1
```
##### 📌 Explicación:
El bucle while se ejecuta mientras la condición sea verdadera (counter < 5).
En cada repetición se imprime el valor y luego se incrementa el contador.
Cuando la condición deja de cumplirse, el bucle se detiene.

###### 🧠 Conceptos clave
- Iteración: cada repetición del bucle
- Condición: en while, determina cuándo termina
- Control: evitar bucles infinitos

👉 Los bucles permiten procesar grandes cantidades de datos de forma automática, lo cual es clave en programación real.





## 🔹 ¿Qué es una lista por comprensión en Python?

Una lista por comprensión (list comprehension) es una forma compacta de crear listas en Python utilizando una sola línea de código.

Permite generar una lista a partir de una secuencia, aplicando transformaciones y condiciones de manera sencilla.

👉 Se utiliza para escribir código más limpio, más expresivo y más eficiente.

### 💻 Ejemplo
```python
numbers = [x for x in range(5)]
```
#### 📌 Explicación:
Crea una lista recorriendo los valores del 0 al 4 usando range(5).
En cada vuelta, el valor de x se añade a la lista automáticamente.
Es una forma más rápida y compacta de crear listas sin usar un bucle for tradicional.

### 💻 Ejemplo con condición
```python
numbers = [x for x in range(10) if x % 2 == 0]
```
#### 📌 Explicación:
Recorre los números del 0 al 9, pero solo añade los que cumplen la condición (x % 2 == 0).
Esto permite filtrar los valores directamente mientras se crea la lista.
El resultado es una lista solo con los números pares.

##### 🧠 ¿Por qué son importantes?
- Reducen la cantidad de código
- Mejoran la legibilidad
- Sustituyen bucles tradicionales en muchos casos

👉 Son muy utilizadas en análisis de datos y manipulación de listas.





## 🔹 ¿Qué es un argumento en Python?

Un argumento es el valor que se pasa a una función cuando esta es llamada. Permite que la función trabaje con datos específicos.

👉 Los argumentos hacen que las funciones sean reutilizables y flexibles.

### 💻 Ejemplo
```python
def greeting(name):
    print("Hi", name)

greeting("Bárbara")
```
#### 📌 Explicación:
En este ejemplo se define una función que recibe un nombre como parámetro.
Cuando se llama a la función con "Bárbara", ese valor se pasa como argumento.
La función utiliza ese argumento para mostrar el mensaje por pantalla.

##### 🧠 Conceptos clave
- Parámetro: variable definida en la función
- Argumento: valor real que se pasa

👉 Gracias a los argumentos, una misma función puede usarse con distintos datos sin necesidad de duplicar código.



## 🔹 ¿Qué es una función Lambda en Python?

Una función lambda es una función anónima (sin nombre) que se define en una sola línea.

👉 Se utiliza para operaciones simples donde no es necesario crear una función completa.

### 💻 Ejemplo
```python
suma = lambda a, b: a + b
    print(suma(2, 3))
```
#### 📌 Explicación:
Se define una función lambda que suma dos valores (a y b).
La función se guarda en la variable suma.
Se ejecuta con 2 y 3 y devuelve 5.

##### 🧠 Características
- No tiene nombre (aunque se puede asignar)
- Se escribe en una sola línea
- Devuelve automáticamente el resultado

👉 Son útiles en operaciones rápidas, como trabajar con listas o funciones internas.



## 🔹 ¿Qué es un paquete pip?

pip es el gestor de paquetes de Python. Permite instalar, actualizar y eliminar librerías externas.

👉 Estas librerías amplían las capacidades de Python.


### 💻 Ejemplo
```bash 
pip install numpy
```
#### 📌 Explicación:
El comando pip install numpy instala una librería externa en Python.
Esta librería añade nuevas funcionalidades, en este caso herramientas para trabajar con números y cálculos.
Gracias a esto, puedes usar código ya creado sin tener que programarlo desde cero.

##### 🧠 ¿Por qué es importante?
- Permite reutilizar código existente
- Acelera el desarrollo
- Facilita trabajar con herramientas avanzadas

###### 🌎 Ejemplos comunes
- numpy --> cálculos matemáticos
- requests --> peticiones HTTP
- flask --> desarrollo web

👉 pip es clave porque conecta los proyectos con el ecosistema de Python.

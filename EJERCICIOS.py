#EJERCICIO 1
for i in range(5):
    print(i)

#EJERCICIO 2
def suma(a, b, c):
    return a + b + c

#EJERCICIO 3
suma_lambda = lambda a, b, c: a + b + c

#EJERCICIO 4
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombre:
    print("El nombre está en la lista")
else:
    print("El nombre NO está en la lista")
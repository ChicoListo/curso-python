#Una lista en Python es una colección ordenada de elementos, que pueden ser de diferentes tipos de datos (números, cadenas, booleanos, etc.).
#Se definen utilizando corchetes [] y los elementos se separan por comas ,.

#crea una lista
mi_lista = [1, 2, 3, 4, 5]

#imprimir la lista
print(mi_lista)

# Acceder al primer elemento de la lista
print(mi_lista[0])

# Acceder al último elemento de la lista
print(mi_lista[-1])

# Acceder a un rango de elementos
print(mi_lista[1:3])

# Modificar el segundo elemento de la lista
mi_lista[1] = 10

# Imprimir la lista modificada
print(mi_lista)

#podemos usar metodos en los arrays como  append(), insert(), remove(), pop(), sort(), reverse()

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)

# Imprimir la lista actualizada
print(mi_lista)

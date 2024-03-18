#llamando a una funcion
def mi_funcion():
    print("Hola desde una funcion")
    
mi_funcion()
#argumentando desde una funcion 
#ejemplo de un solo argumento
def funcion_name(fname):
    print(fname + " ")

funcion_name("Emilio")
funcion_name("Tobias")
funcion_name("Linux")

#Ejemplo de dos argumentos

def la_funcion(fname, sname):
    print(fname + " " + sname)
la_funcion("Emilio", "Tobias")

# agregamos un asterisco si deseamos agregar elementos arbitrariamente en forma de tupla, si se agregan 2 seria en forma de diccionario
def args_funcion (*niños):
    print("El niño mas pequeño es " + niños[2])

args_funcion("Emilio", "Tobias", "Linux")

#argumentos con keyword 
def key_funcion(niño1, niño2, niño3):
    print("El niño mas pequeño es " + niño3)

key_funcion(niño1="Emilio", niño2="Tobias", niño3="Linux")

#Usar un valor por default

def def_funcion(pais = "Brasil"):
    print("Yo soy de " + pais)

def_funcion("Mexico")
def_funcion("Argentina")
def_funcion("Chile")
def_funcion()

#pasar una lista como un argumento
def ls_funcion(comida):
    for x in comida:
        print(x)
    
frutas =["Manzana", "Platano", "Aguacate"]

ls_funcion(frutas)

#Valores de retorno
def ret_funcion(x):
    return 7 * x

print(ret_funcion(9))
print(ret_funcion(7))
print(ret_funcion(4))

#con pass podemos evitar errores con funciones vacias 

def emp_funcion():
    pass
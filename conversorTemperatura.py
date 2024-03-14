temperatura = input("ingresa la temperatura a convertir:    ")
unidad = input("celcius (c) o farenheit (f):  ").lower()

numerotemp = float(temperatura)

if unidad == "c":
    fahrenheit = (numerotemp - 32) * 5/9
    print("fahrenheit: ")
    print(fahrenheit)

elif unidad == "f":
    centigrados = (numerotemp * 5/9) + 32
    print("Centigrados:")
    print (centigrados)
else:
    print("verifique su informacion.")
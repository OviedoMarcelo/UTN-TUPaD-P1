#-----------------Zona de Funciones-----------------------#

# 1) Crear una función llamada imprimir_hola_mundo
def imprimir_hola_mundo () :
    """
    Imprime: “Hola mundo.”

    """
    print("Hola mundo")

# 2) Crear una función llamada saludar_usuario(nombre)

def saludar_usuario(nombre):
    """
    Imprime: “Hola [nombre].”
    
    """
    print(f"Hola {nombre}.")

# 3) Crear una función llamada informacion_personal(nombre, apellido,edad, residencia)

def informacion_personal(nombre, apellido , edad, residencia):
    """
    Imprime: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”

    """
    print(f"Soy {nombre} {apellido}, tendo {edad} años y vivo en {residencia}")

# 4) Crear dos funciones: calcular_area_circulo(radio)
#   calcular_perimetro_circulo(radio)

def calcular_area_circulo(radio):
    """
    Retorna el área de un círculo recibido su radio. 
            Área = π * r^2
    
    """
    from math import pi,pow
    return(pi * pow(radio,2))

def calcular_perimetro_circulo(radio):
    """
    Retorna el perímetro de un círculo recibido su radio. 
            Perímetro = 2 * r * π
    """
    from math import pi
    return(2 * radio * pi)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    """
    Retorna la cantidad de horas que representan los segundos recibidos. 
            s / 3600
    """
    return (segundos/3600)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar del numero

    """
    print(f"""----------------------------
Tabla de Multiplicar de {numero}
    {numero} * 0 = {numero*0}
    {numero} * 1 = {numero*1}
    {numero} * 2 = {numero*2}
    {numero} * 3 = {numero*3}
    {numero} * 4 = {numero*4}
    {numero} * 5 = {numero*5}
    {numero} * 6 = {numero*6}
    {numero} * 7 = {numero*7}
    {numero} * 8 = {numero*8}
    {numero} * 9 = {numero*9}
    {numero} * 10 = {numero*10}
----------------------------""")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a:int, b:int):
    """
    Devuelve en una tupla (suma, resta, multiplicacion, division entera)
    el resultado de hacer dichas operaciones entre a y b

    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b if b != 0 else None

    return (suma, resta, multiplicacion, division)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc (peso: float, altura: float) :
    """
    Devuelve el valor del indice de masa muscular 
    
    """
    return(peso/altura**2)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius:float):
    """
    Devuelve el equivalente a fahrenheit recibidos
    
    """
    return (9/5 * celsius + 32)


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función

def calcular_promedio(*numeros: float) :
    """
    Devuelve el promedio de los números recibidos
    
    """
    if len(numeros) == 0: #esta condición la pongo por si se invoca sin parámetros
        return 0
    else:
        return (sum(numeros)/len(numeros))





#-------------------Programa principal---------------------#
# 1) Invocamos hola mundo
imprimir_hola_mundo()

# 2) Invocamos saludar usuarios
saludar_usuario("Marcelo")

# 3) Invocamos información personal y solicitamos el ingreso de datos por el usuario
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia) 

# 4) Invocamos las funciones para calcular area y calcular perimetro
radio = float(input("Ingrese el radio de su círculo para conocer su área y perímetro"))
print(f"El área del círculo con radio: {radio} es de: {calcular_area_circulo(radio):.2f} y si perímetro es de: {calcular_perimetro_circulo(radio):.2f}")



# 5) Invocamos una llamada a la función segundos_a_horas() que convierte segundos a horas
seg = int(input("Ingrese la cantidad de segundos que quiere convertir a horas"))
print(f"{seg} equivanlen a {segundos_a_horas(seg):.2f} horas")

# 6) Invocamos a la función que imprime la tabla de un número
print("Bienvenido al programa que imprime la tabla de multiplicar")
numero = int(input("Ingrese el número del cual quiere ver la tabla: "))
tabla_multiplicar(numero)


# 7) Invocamos la operación de operaciones_basicas

print("Bienvenido al programa de operaciones básicas entre 2 valores.")
a = int(input("Ingrese el primer operador: "))
b = int(input("Ingrese el segundo operador: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print(f"Suma {a} + {b} = {suma}  ")
print(f"Resta {a} - {b} = {resta}: ")
print(f"Multiplicación {a} * {b} = {multiplicacion}: ")
print(f"División {a} / {b} = {division} ") if multiplicacion else print (f"{a}/ {b} = Error no se puede dividir por cero")

# 8) Invocamos la función para calcular el indice de masa corporal

print ("Bienvenido al programa de cálculo de índice de masa corporal")
peso = float(input("Ingrese su peso en kg"))
altura = float(input("Ingrese su altura en metros"))
print(f"Su índice de masa corporal IMC es {calcular_imc(peso, altura):.2f}")

# 9) Invocamos la función para convertir celsius a fahrenheit

print("Bienvenido al programa de conversión de grados C° a grados F°")
celsius = float(input("Ingrese los grados Celsius a convertir: "))
print(f"{celsius}°C equivalente a {celsius_a_fahrenheit(celsius):.1f}°F")

# 10) Invoco la función promedio que convertí para que sirva para cualquier cantidad numeros

print(f"El promedio para 10, 25, 30 y 40 es: {calcular_promedio(10,25,30,40)}")
print(f"El promedio para 1, 10 es: {calcular_promedio(1,10):.2f}")
print(f"El promedio para 99, 0 es: {calcular_promedio(1,10):.2f}")
print(f"El promedio para 10,20,60,40,98,88,70 es: {calcular_promedio(10,20,60,40,98,88,70):.2f}")
print(f"El promedio para 0 es: {calcular_promedio(0):.2f}")
print(f"El promedio para es: {calcular_promedio():.2f}")





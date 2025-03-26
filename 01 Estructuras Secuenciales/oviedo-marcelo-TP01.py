# 1 Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("¡Hola Mundo!")

# 2 Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado

nombre = input("Bienvenido, ingrese su nombre para continuar")
print(f"Hola {nombre}, bienvenido")

# 3 Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados
nombre = input("Ingrese su nombre: ")
apellido = input(f"Ahora {nombre} ingrese su apellido por favor: ")
edad = input(f"Por favor {nombre}, ahora ingresa tu edad: ")
residencia = input(f"Para finalizar {nombre}, ahora ingrese su lugar de residencia por favor: ")
#imprimo la frase concatenada
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4  Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

print ("Bienvenido al programa para calcular el área y perímetro de un círculo ingresado su radio")
#Defino el valor de pi, podría usar la librería de math pero simplifico. 
pi = 3.1416
radio = float(input ("Ingrese el radio del círculo: "))
#Cuando imprimo utilizo el :2f para mostrar solo 2 decimales
print(f"El área del círculo de radio: {radio} es igual a {pi*radio**2:.2f}")
print(f"El perímetro del círculo de radio: {radio} es igual a {2*pi*radio:.2f}")

# 5  Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
print ("Bienvenido al programa para calcular a cuantas horas equivalen los segundos ingresados")
segundos = int(input("Ingrese los segundos que quiera convertir a horas: "))
print(f"{segundos} segundos equivale a {segundos/3600:.2f} horas.")

# 6 Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("Bienvenido al programa de tablas de multiplicar.")
numero = int(input("Ingrese un número y mostraremos su tabla de multiplicar del 0 al 10: "))
print(f"""----------------------------
Tabla de Multiplicar del {numero}
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
----------------------------"""
)

# 7 Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print ("Bienvenido a este programa. Ingrese 2 números y mostraremos el resultado de hacer cuentas entre ellos")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"""----------------------------
    Operaciones
    {num1} + {num2} = {num1+num2}
    {num1} - {num2} = {num1-num2}
    {num1} * {num2} = {num1*num2}
    {num1} / {num2} = {num1/num2}
----------------------------""")

#8 Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC = pesokg/alturam**2
print ("Bienvenido al programa de cálculo de índice de masa corporal")
peso = float(input("Ingrese su peso en kg"))
altura = float(input("Ingrese su altura en metros"))
print(f"Su índice de masa corporal IMC es {peso/altura**2:.2f}")

# 9 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia: F° = 9/5*C°+32
print("Bienvenido al programa de conversión de grados C° a grados F°")
celsius=int(input("Ingrese los grados Celsius a convertir: "))
print(f"{celsius}°C equivalente a {9/5 * celsius + 32}F°")


# 10  Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("Bienvenido a este programa para calcular el promedio de 3 números ingresador")
num1 = int(input ("Ingrese por favor el primer número: "))
num2 = int(input ("Ingrese por favor el segundo número: "))
num3 = int(input ("Ingrese por favor el tercer número: "))
print(f"El promedio de los números {num1},{num2},{num3} es {(num1+num2+num3)/3}")



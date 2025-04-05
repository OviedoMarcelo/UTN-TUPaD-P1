#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
print("Bienvenido al programa que determina si ustedes es mayor de edad.")
edad = int(input("Ingrese su edad: "))
print (f"Usted es mayor de edad a sus {edad} años") if edad >=18 else print(f"Usted no es mayor de edad.")

#---------------------------------------------------------#
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

print("Bienvenido al programa que determina si aprobó la materia.")
nota = int(input("Ingrese su nota: "))
print (f"Felicitaciones ¡Usted ha aprobado!") if nota >=6 else print(f"¡Lo sentimos! Usted no ha aprobado. Siga esforzándose.")

#---------------------------------------------------------#
# 3)Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
print("Bienvenido al programa para determinar si el número ingresado es par.")
numero=int(input("Por favor ingrese un número"))
print(f"El número ingresado {numero} es par") if numero % 2 == 0 else print(f"El número ingresado {numero} es impar.")

#---------------------------------------------------------#
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

print("Bienvenido al programa para determinar en que grupo etario te encuentras 😁")
edad = int(input("Por favor ingrese su edad"))
if edad < 0:
    print("Usted ingresó una edad no válida: {edad}") 
elif edad <12:
    print(f"La edad ingresada es {edad} pertenece al grupo Niño/a")
elif edad < 18 :
    print(f"La edad ingresada es {edad} pertenece al grupo Adolescente")
elif edad < 30 :
    print(f"La edad ingresada es {edad} pertenece al grupo Adulto/a Joven")
else:
    print(f"La edad ingresada es {edad} pertenece al grupo Adulto/a")

#---------------------------------------------------------#
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
print("Bienvenido al programa para el ingreso de su password")
password = input("Por favor ingrese una contraseña válida entre 8 y 14 caracteres: ")
#Uso operador ternacio
print("Ha ingresado una contraseña correcta") if len(password) >=8 and len(password)<=14 else print("Por favor ingrese una contraseña válida entre 8 y 14 caracteres")

#---------------------------------------------------------#
# 6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#importo las librerías necesarias
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#calculo moda, mediana y media de la lista aleatoria
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print(f"Distribución con sesgo positivo ya que media={media} mayor que mediana={mediana} y mediana mayor que moda={moda}")
elif media < mediana and mediana < moda: 
    print(f"Distribución con sesgo negativo ya que media={media} menor que mediana={mediana} y mediana menor que moda={moda}")
elif media == mediana == moda: 
    print(f"Distribución sin sesgo ya que media={media} mediana={mediana} y moda={moda}")
else:
    print(f"No se puede determinar el sesgo ya que media={media} mediana={mediana} y moda={moda}.")

#---------------------------------------------------------#
#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
print("Programa para agregar un signo de exclamación a la palabra o frase si termina en vocal")
texto = input("Ingrese una palabra o frase")
ultima_letra = texto[-1] #Me quedo con la ultima letra de la cadena
if ultima_letra.lower() in "aeiou" : #me fijo si encuentro esa letra entre las vocales en minúscula
    print(texto+"!")
else:
    print(texto)

#---------------------------------------------------------#
# 8)  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
print("Bienvenido al programa para darle formato a su nombre")
nombre = input("Ingrese nu nombre: ")
opcion = int(input("""Ahora ingrese una opción:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."""))
if opcion==1:
    print(f"Su nombre es {nombre.upper()}")
elif opcion ==2:
    print(f"Su nombre es {nombre.lower()}")
elif opcion ==3:
    print(f"Su nombre es {nombre.title()}")
else:
    print("Usted ingresó una opción no válida. Intente nuevamente.")


#---------------------------------------------------------#
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
print("Bienvenido al programa para informar el detalle de la magnitud de un terremoto.")
magnitud = int(input("Ingrese la magnitud del terrmoto ocurrido."))
if magnitud < 3 :
    print(f'Magnitud:{magnitud} "Muy leve" (imperceptible)')
elif magnitud < 4: 
    print(f'Magnitud:{magnitud} "Leve" (ligeramente perceptible)')    
elif magnitud < 5:
    print(f'Magnitud:{magnitud} "Moderado" (sentido por personas, pero generalmente no causa daños)')
elif magnitud <6:
    print(f'Magnitud:{magnitud} "Fuerte" (puede causar daños en estructuras débiles)')
elif magnitud < 7:
    print(f'Magnitud:{magnitud} "Muy Fuerte" (puede causar daños significativos)')
else:
    print(f'Magnitud:{magnitud} "Extremo" (puede causar graves daños a gran escala)')

#---------------------------------------------------------#
# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
print("Bienvenido al programa para determinar en que estación del año te encuentras")
hemisferio = input("""Ingrese en que hemisferio se encuentra: 
S = Sur 
N = Norte""")
mes = int(input("Ingrese el mes del año (1 a 12)"))
dia = int(input("Ingrese el día del año (1 a 31)"))

# Determinar estación según la fecha y el hemisferio
if hemisferio.lower() == "n":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Verano")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Otoño")
    else:
        print("Fecha inválida")

elif hemisferio.lower() == "s":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print(f"La estación del año para {dia}/{mes} en el hemisferio: {hemisferio} es: Primavera")
    else:
        print("Fecha inválida")
else:
    print("Hemisferio inválido")

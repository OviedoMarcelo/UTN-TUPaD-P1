#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100   
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
num=100
print(f"Bienvenido al siguiente programa. Se imprimiran los números del 0 hasta el {num}:")
for i in range (num+1) :
    print(i)

#------------------------------------------------------------------------------------------#
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
print("Bienvenido al programa que dado un número entero indicará cuantos dígitos contiene.")
cantDigitos=0
num=int(input("Ingrese un número entero: "))
#Me aseguro que el número cuando lo trate sea positivo
digitosNum = abs(num)
if digitosNum == 0:
    cantDigitos+=1
else:
    while digitosNum > 0: 
        cantDigitos+=1
        digitosNum = digitosNum //10
print (f"El número ingresado {num} tiene {cantDigitos} digito/s")


#------------------------------------------------------------------------------------------#
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("Bievenido al programa para sumar los números entre 2 rangos de números brindados (excluyendo los ingresados)")
num1 = int(input("Ingrese el número inicial: "))
num2 = int(input("Ingrese el segundo número: "))
suma=0
for i in range (num1+1,num2):
    suma+=i
    print(i)
print(f"La suma total de los números comprendidos entre {num1} y {num2} es {suma}")

#------------------------------------------------------------------------------------------#
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
print("Bievenido al programa para sumar los números ingresados hasta ingresar un número cero. Se sumara cualquier número entero (positivo o negativo)")
suma= 0
num=int(input("Ingrese un número: "))
while num != 0 :
    suma+=num
    num=int(input("Ingrese un número: "))
print(f"Se ingresó el cero el programa finaliza.")
print(f"La suma total de los números que fueron ingresando es de {suma}")

#------------------------------------------------------------------------------------------#
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numeroAdivinar = random.randint(0,9)
adivino=False
while not adivino: 
    num=int(input("Ingrese un número del 0 al 9. ¡Buena Suerte!🍀:  "))
    if num == numeroAdivinar:
        adivino = True
    else:
        print(f"El número ingresado {num} no es correcto.")
print(f"¡Felicitaciones usted adivinó! El número a adivinar era {numeroAdivinar} y usted ingresó {num}")

#------------------------------------------------------------------------------------------#
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
num1=0
num2=100
print(f"Bienvenido. Imprimiremos todos los números pares en forma decreciente entre {num1} y {num2}")
#Se considera al 0 como número par, por ende como es decreciente resto 1 al numero hasta para que lo considere
for i in range (num2,num1-1,-2) : 
    print(i)
print("Fin del programa")

#------------------------------------------------------------------------------------------#
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("Bienvenido, imprimiremos en pantalla todos los números pares comprendidos entre el 0 y el números que usted nos indique")
num = int(input("Ingrese el numero hasta el que quiere que contemos, recuerde ingrese un número entero positivo"))
if num <= 0 :
    print(f"El numero ingresado {num} no es válido, ingrese un número positivo.")
else : 
    print(f"Números pares comprendidos entre el 0 y el {num}:")
    for i in range (0 , num+1 , 2) :
        print (i,end="-")
print()
print ("Fin del programa")

#------------------------------------------------------------------------------------------#
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
numeros_a_ingresar = 5
numeros_pares = 0
numeros_impares = 0
numeros_negativos = 0
numeros_positivos = 0
print(f"Bienvenido al siguiente programa, donde ustedes ingresará {numeros_a_ingresar} e indicaremos el total de numeros pares, impares, positivos y negativos")
print("¡A comenzar!")
for i in range (0,numeros_a_ingresar) :
    numero = int(input(f"Ingrese el {i+1}° número: "))
    if numero >=0:
        numeros_positivos+=1
    else:
        numeros_negativos+=1
    if numero % 2 == 0:
        numeros_pares+=1
    else:
        numeros_impares+=1
print(f"Ingresaron un total de {numeros_a_ingresar} números.")
print(f"{numeros_pares} de ellos fueron pares.")
print(f"{numeros_impares} de ellos fueron impares.")
print(f"{numeros_negativos} de ellos fueron negativos.")
print(f"{numeros_positivos} de ellos fueron positivos.")
print("Fin del programa")

#------------------------------------------------------------------------------------------#
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
numeros_a_ingresar = 5
suma_de_valores = 0
print(f"Bienvenido. Le pediremos que ingrese {numeros_a_ingresar} números para calcular su media")
for i in range (0,numeros_a_ingresar):
    suma_de_valores += int(input(f"Ingrese el {i+1}° número"))
media = suma_de_valores /numeros_a_ingresar
print(f"La media o promedio de los {numeros_a_ingresar} números ingresados es de {media}")

#------------------------------------------------------------------------------------------#
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("Bienvenido, al ingresar usted un número invertiremos el orden de los dígitos")
numero_ingresado = int(input("Ingrese el número que desea invertir: "))
numero_invertido = 0
numero = abs(numero_ingresado)
negativo = False
if numero_ingresado < 0:
    negativo = True
while numero > 0 :
    digito = numero % 10 #me quedo con el último número (el resto)
    numero_invertido = numero_invertido * 10 + digito #le "agrego" un cero al final por cada iteración y sumo el último digito
    numero = numero // 10
if negativo == True:
    numero_invertido*=-1
print (f"El número {numero_ingresado} invertido es {numero_invertido}")
from funciones_recursivas import contar_digitos_rec as contar_digitos

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 

print(f"Bienvenido al programa que contará la occurrencia de un dígito en un número dado")
try:
    numero = int(input("Ingrese un número entero: "))
    digito = int(input("Ahora ingrese el dígito que quiera verificar cuantas ocurrencias tiene: "))
    print(f"El digito {digito} aparece {contar_digitos(numero,digito)} en el número {numero}")
except:
    print("Error: usted ingresó un valor incorrecto. Fin del programa.")
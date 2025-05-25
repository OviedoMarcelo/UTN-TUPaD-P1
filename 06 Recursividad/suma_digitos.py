from funciones_recursivas import suma_digitos_rec as suma_digitos

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

print(f"Bienvenido al programa para sumar los dígitos de un número entero dado")
try:
    numero = int(input("Ingrese el número que quiera sumar sus dígitos: "))
    print(f"La suma de todos los dígitos del número {numero} es {suma_digitos(numero)}")
except:
    print("Usted no ingresó un número entero válido")
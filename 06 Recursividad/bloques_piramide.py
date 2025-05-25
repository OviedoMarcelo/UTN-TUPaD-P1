from funciones_recursivas import contar_bloques_rec as contar_bloques

# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

print(f"Bienvenido al programa que calcula la cantidad de bloques necesario para construir una piramide dada la base.")
try:
    base = int(input("Ingrese el número de bloques en la base de la pirámide: "))
    print(f"La cantidad de bloques necesarios para constuir una pirámide de base {base} es de {contar_bloques(base)}")
except:
    print("No se ingreso un valor válido para la base. Debe ser un número entero.")
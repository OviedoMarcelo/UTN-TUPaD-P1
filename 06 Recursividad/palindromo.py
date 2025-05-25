from funciones_recursivas import palindromo_rec as palindromo
# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

print(f"Bienvenido al programa que verifica si una palabra es palíndroma")
palabra = input("Ingresa la palabra que quiera validar: ")
if palindromo(palabra):
    print(f"La palabra {palabra} es palindroma")
else:
    print(f"la plabra {palabra} no es palíndroma")
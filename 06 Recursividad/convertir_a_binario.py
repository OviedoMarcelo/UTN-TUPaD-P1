from funciones_recursivas import convertidor_a_binario_rec as convertidor_binario

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

try:
    print("Bienvenido al programa para convertir decimales a enteror")
    decimal = int(input("Ingrese un numero entero: "))
    print(f"El número {decimal} en binario es: {convertidor_binario(decimal)}")
except:
    print(f"Usted ingresó un número no válido. El número {decimal} no corresponde a un entero.")
from funciones_recursivas import factorial_rec as factorial

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
print(f"Bienvenido el programa para calcular factoriales.")
num = int(input("Ingrese el número del cual quiere calcular el factorial entre 1 el número ingresado: "))
for num in range(1,num+1):
    print(f"El factorial de {num} es: {factorial(num)}")

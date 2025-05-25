from funciones_recursivas import fibonacci_rec as fibonacci

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

print(f"Bienvenido el programa para calcular la serie de fibonacci dado un número.")
pos =  int(input("Ingrese la posición de la cual quiera conocer el valor en la serie de fibonacci: "))
print(f"La posición {pos} corresponde al valor {fibonacci(pos)}")
print(f"Serie de fibonacci completa hasta la posición {pos}: ")
for i in range(1,pos+1):
    print(fibonacci(i),end=" ")
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range
multiplo=4
lista_multiplos = list(range(multiplo,101,multiplo))
print(lista_multiplos)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo

lista = ["rojo", "amarillo","azul","verde","morado","dorado"]
print(lista[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla

lista = []
print(lista)
lista.append("Hola")
lista.append("Bienvenido")
lista.append("Adios")
print(lista)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!


animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista de animales: {animales}")
animales[1]="loro"
animales[-1]="oso"
print(f"Lista de actualizada: {animales}")

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7] ---> Genera una lista con 5 elementos, el numero 8,15,3,22 y 7
# numeros. remove (max (numeros ) ) ----> remueve el elemento devuelvo por la función max de números, que en este caso sería el número más grande de la lista el 22
# print (numeros) ---> imprime de nuevo la lista que será 8,15,3 y 7

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
lista = list(range(10,31,5))
print(f"Lista: {lista}")

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
print(f"Lista original: {autos}")
index_valor_central=(int(len(autos))//2-1) #obtengo el largo de la lista, busco la mitad entera y resto 1
autos[index_valor_central] = "Trend"
autos[index_valor_central+1] = "Fox"
print(f"Lista nueva: {autos}")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
print(f"Lista original: {dobles}")
for i in range(5,16,5):
    dobles.append(i*2)
print(f"Lista modificada: {dobles}")

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
print(f"Lista de compras original:")
print(compras)
compras[2].append("jugo")
print(f"Agrego jugo al 3er cliente")
print(compras)
compras[1][compras[1].index("fideos")] = "tallarines"
print(f"Cambio fideos por tallarines en 2do cliente:")
print(compras)
compras[0].remove("pan")
print(f"Elimino Pan de la lista del primer cliente:")
print(compras)
from funciones_recursivas import potencia_rec as potencia

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general.


print(f"Bienvenido al program para calcular potencias")
base = int(input("Ingrese el número base que quiere elevar: "))
exponente = int(input("Ingrese el exponente de la base: "))
print(f"El resultado de {base} elevado a la {exponente} es: {potencia(base,exponente)}")
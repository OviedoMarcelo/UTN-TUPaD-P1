#Función factorial recursiva

def factorial_rec(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial_rec(num-1)

#Función fibonacci recursiva

def fibonacci_rec(posicion):
    if posicion == 1: 
        return 1
    elif posicion == 0:
        return 0
    else:
        return fibonacci_rec(posicion-1) + fibonacci_rec(posicion-2)
    

#Función recursiva para potencias
def potencia_rec(n,m):
    if m == 0: #caso base de potencia de 0 = 1 
        return 1
    else:
        return n * potencia_rec(n,m-1)
    

#Función recursiva para convertir entero a binario
def convertidor_a_binario_rec(dec):
    if dec ==1:
        return "1"
    elif dec == 0:
        return "0"
    else:
        return convertidor_a_binario_rec(dec//2)+str(dec%2)
    
#Función recursiva para entender un palindromo.
def palindromo_rec(palabra):
    if len(palabra) == 1 or len(palabra)==0:
        return True
    elif palabra[0]!=palabra[-1] :
        return False
    else:
        return palindromo_rec(palabra[1:-1])

#Función recursiva para sumar dígitos de un número
def suma_digitos_rec(digito):
    if digito == 0:
        return 0
    else:
        return digito%10+suma_digitos_rec(digito//10)
    

#Funcion recursiva para contar bloques necesarios para contruir una piramide
def contar_bloques_rec(base):
    if base == 1: 
        return 1
    else:
        return base+contar_bloques_rec(base-1)
    
#Función recursiva para contar digitos en un numero 
def contar_digitos_rec (numero, digito):
    if numero == 0:
        return 0
    elif numero%10 == digito:
        return 1+ contar_digitos_rec(numero//10,digito)
    else:
        return contar_digitos_rec(numero//10,digito)

#Zona de pruebas
if __name__ == "__main__":
    print(contar_digitos_rec(1,9))
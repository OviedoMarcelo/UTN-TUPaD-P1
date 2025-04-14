# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print(precios_frutas)
#Genero un nuevo diccionario con las frutas a agregar
frutas_a_agregar = {'Naranja': 1200, 'Manzana': 1500}
precios_frutas.update(frutas_a_agregar) #Uso el método update de los diccionarios
precios_frutas['Pera'] = 2300 #Uso el método para agregar individualmente
print(precios_frutas)

#------------------------------------------------------------------------------#
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#------------------------------------------------------------------------------#
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
lista_frutas = []
for e in precios_frutas:
    lista_frutas.append(e)
print(lista_frutas)

#lista_frutas = list(precios_frutas.keys()) #Alternativa más directa, usando este metodo de los dic
#print(lista_frutas)

#------------------------------------------------------------------------------#

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
# años."

class Persona:
    """
    Clase persona.
    """
    #   Constructor de la clase
    def __init__ (self, nombre, pais, edad):
        """
        Constructor de la clase persona.
        """
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    
    #   Le agrego este método que permite que se imprima directamente como un string el objeto.
    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - {self.pais}"
    
    #   Métodos
    def saludar (self):
        """
        Metodo que imprime en pantalla un saludo con la info de la persona.
        """
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

persona = Persona("Marcelo", "Argentina",33)
persona.saludar()
print(persona)

#------------------------------------------------------------------------------#

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
from math import pi
class Circulo :
    """
    Clase que representa un círculo geométrico.
    """

    def __init__(self, radio:float):
        """
        Constructor que requiere radio.
        """
        self.radio = radio
    
    def __str__(self):
        """
        String para imprimir el objeto. 
        """
        
        return(f"Circulo de radio: {self.radio}")

    #   Métodos

    def calcular_area (self) :
        """
        Retorna el área.
        """    
        return (pi*self.radio**2)


    def calcular_perimetro (self) :
        """
        Retorna el perímetro.
        """  
        return (2 * self.radio * pi)
    
#------------------Area de prueba--------------------#

circulo = Circulo(2.5)
print(f"El área del {circulo} es de {circulo.calcular_area():.2f} y su perímetro es de {circulo.calcular_perimetro():.2f}")


#------------------------------------------------------------------------------#

# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
# balanceados usando una pila.

class Pila:
    """
    Clase que representa una pila.
    """
    
    def __init__(self):
        """
        Constructor
        """
        self.elementos = []

    # Metodos

    def apilar(self, elemento):
        """
        Apila un nuevo elemento
        """
        self.elementos.append(elemento)

    def desapilar(self):
        """
        Retorna el elemento del tope de la pila, eliminando el mismo.
        """
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        """
        Retorna si la pila contiene elementos.
        """
        return len(self.elementos) == 0

    def ver_tope(self):
        """
        Retorna el elmento del tope de pila (sin eliminar)
        """
        if not self.esta_vacia():
            return self.elementos[-1]
        return None

#Función para verificar caracteres balanceados usando pila

def balanceado (cadena: str):
    pila = Pila()
    #Genero un diccionario para encontrar fácil el de apertura y cierre.
    pares = {')': '(', ']': '[', '}': '{'}
    for caracter in cadena:
        if caracter in "([{": #si el caracter que encuentro es de apertura apilo
            pila.apilar(caracter)
        elif caracter in ")]}": #si el caracter que tengo es uno de cierre
            if pila.esta_vacia() or pila.desapilar()!= pares[caracter]: #si la pila esta vacía (no esta el caracter de apertura) o el elemento no corresponde al cierre no esta balanceado
                return False # por ende devuelvo falso
    return pila.esta_vacia() #si al final de recorrer toda la cadena la pila esta vacía esta balanceado, caso contrario quedó un caracter no balanceado.


#---------Zona de pruebas-------------------#

print(balanceado('[{()}]')) #True
print(balanceado('[]{}}')) #False
print(balanceado('[{{[}]}}]')) #False
print(balanceado('[[]]{}'))#True
print(balanceado('[')) #False


#------------------------------------------------------------------------------#

# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# ● Agregar clientes (encolar).
# ● Atender clientes (desencolar).
# ● Mostrar el siguiente cliente en la fila
from collections import deque
class ColaBancaria :
    """
    Clase que permite manejar una cola
    """
    def __init__(self):
        """
        Constructor.
        """
        self.elementos = deque()

    def __str__(self):
        """
        Permite imprimir el objeto.
        """
        return (f"{self.elementos}")

    def esta_vacia(self):
        """
        Retorna si la cola tiene elementos
        """
        return len(self.elementos) == 0
    
    def agregar_cliente (self, elemento):
        """
        Agrega un elemento a la cola
        """
        return self.elementos.append(elemento)

    def atender_cliente (self):
        """
        Retorna y extrae el primer elemento de la cola.
        """
        if not self.esta_vacia():
            return self.elementos.popleft()
        
    def ver_siguiente (self):
        """
        Retorna el primer elemento de la cola
        """
        return self.elementos[0] if not self.esta_vacia() else []
        
# Zona de pruebas # 

cola_de_atencion = ColaBancaria()
cola_de_atencion.agregar_cliente("Cliente 1")
cola_de_atencion.agregar_cliente("Cliente 2")
cola_de_atencion.agregar_cliente("Cliente 3")
cola_de_atencion.agregar_cliente("Cliente 4")
cola_de_atencion.agregar_cliente("Cliente 5")
#Ver el siguiente cliente, debería ser el 1
print(cola_de_atencion.ver_siguiente())
#Lo atiendo
cola_de_atencion.atender_cliente()
print(cola_de_atencion)
#Agrego un nuevo cliente debería ir al final de la cola 
cola_de_atencion.agregar_cliente("Cliente 6")
print(cola_de_atencion)
#Atiendo a todos
cola_de_atencion.atender_cliente()
print(cola_de_atencion)
cola_de_atencion.atender_cliente()
print(cola_de_atencion)
cola_de_atencion.atender_cliente()
print(cola_de_atencion)
cola_de_atencion.atender_cliente()
print(cola_de_atencion)
cola_de_atencion.atender_cliente()
print(cola_de_atencion)





# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
# los valores almacenados.



class Nodo:
    """
    Nodo de una lista enlazada simple
    """
    def __init__(self, dato=None):
        """
        Constructor de la case nodo para una lista enlazada simple
        """
        self.dato = dato #Valor del nodo
        self.siguiente = None #Puntero el siguiente nodo inicia siempre vacío

class ListaEnlazada:
    """
    Lista Enlazada simple
    """
    def __init__(self):
        self.cabeza = None #La lista se inicializa vacía.

    def insertar(self, dato):
        """
        Inserta un nuevo nodo en la lista y lo enlaza con el dato recibido.
        """
        nuevo_nodo = Nodo(dato) #Genero el nuevo nodo
        nuevo_nodo.siguiente = self.cabeza #el nuevo nodo apunta a la actual "cabeza de la lista"
        self.cabeza = nuevo_nodo #Ahora la nueva cabeza de la lista es el recientemente agregado
    
    def recorrer_la_lista(self):
        """
        Recorre e imprime la lista.
        """
        actual = self.cabeza #arranco desde el nodo inicial
        while actual: #mientras haya un elemento valido
            print(actual.dato, end= ' -> ')
            actual = actual.siguiente
        print("Fin")

# Zona de pruebas 

lista_enlazada = ListaEnlazada()
lista_enlazada.insertar('4️⃣')
lista_enlazada.insertar('3️⃣')
lista_enlazada.insertar('2️⃣')
lista_enlazada.insertar('1️⃣')
lista_enlazada.recorrer_la_lista()

#------------------------------------------------------------------------------#
# 9) Dada una lista enlazada, implementa una función para invertirla.

def invertir_lista_enlazada(lista:ListaEnlazada):
    lista_invertida = ListaEnlazada()
    actual = lista.cabeza

    while actual is not None: #mientras no llegue al último elemento
        nuevo_nodo = Nodo(actual.dato)  # Creamos un nodo nuevo con nodo en el que esto parado
        nuevo_nodo.siguiente = lista_invertida.cabeza #Pongo como siguiente el que esta en la cabecera de la invertida
        lista_invertida.cabeza = nuevo_nodo #El nuevo nodo queda como cabeza
        actual = actual.siguiente #agarro el siguiente nodo

    return lista_invertida

# Zona de pruebas #
lista_invertida = invertir_lista_enlazada(lista_enlazada)
lista_invertida.recorrer_la_lista()

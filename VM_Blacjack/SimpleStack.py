# Implement a Stack data structure using a Python list
import random
class Stack(object):
     def __init__(self, max): # Constructor
      self.__stackList = [None] * max  # The stack stored as a list
      self.__top = -1  # No items initially

     def push(self, item):  # Insert item at top of stack
         self.__top += 1  # Advance the pointer
         self.__stackList[self.__top] = item  # Store item

     def pop(self):  # Remove top item from stack
         top = self.__stackList[self.__top]  # Top item
         self.__stackList[self.__top] = None  # Remove item reference
         self.__top -= 1  # Decrease the pointer
         return top  # Return top item

     def clear(self):
         # Vaciar la pila haciendo pop hasta que esté vacía
         while not self.isEmpty():
             self.pop()  # Hace pop de los elementos hasta que la pila esté vacía

     def peek(self):  # Return top item
         if not self.isEmpty():  # If stack is not empty
             return self.__stackList[self.__top]  # Return the top item

     def isEmpty(self):  # Check if stack is empty
         return self.__top < 0

     def isFull(self):  # Check if stack is full
         return self.__top >= len(self.__stackList) - 1

     def __len__(self):  # Return # of items on stack
         return self.__top + 1

     def __str__(self):  # Convert stack to string
         ans = "["  # Start with left bracket
         for i in range(self.__top + 1):  # Loop through current items
           if len(ans) > 1:  # Except next to left bracket,
              ans += ", "  # separate items with comma
           ans += str(self.__stackList[i])  # Add string form of item
         ans += "]"  # Close with right bracket
         return ans

     def swap(self):
         """Método para reorganizar aleatoriamente los elementos en la pila"""
         # Extraer todos los elementos de la pila en una lista temporal
         temp_list = []
         while not self.isEmpty():
             temp_list.append(self.pop())

         # Mezclar los elementos de la lista de forma aleatoria
         random.shuffle(temp_list)

         # Colocar los elementos de vuelta en la pila en orden aleatorio
         for item in temp_list:
             self.push(item)
     # Función auxiliar para obtener el valor del primer carácter


def obtener_valor(carta, contador_actual):
    # Tomar el primer dígito o letra de la carta
    primer_caracter = carta[0]

    # Verificar si es una letra J, Q, K que valen 10
    if primer_caracter in ['J', 'Q', 'K']:
        return 10
    # Verificar si es un As (A) y ajustar el valor basado en el contador actual
    elif primer_caracter == 'A':
        return 11 if contador_actual <= 10 else 1
    # Si es un número entre 2 y 9, convertirlo a entero
    elif primer_caracter.isdigit() and primer_caracter != '1':  # Excluir el '10'
        return int(primer_caracter)
    # Asumir que si no es J, Q, K o un número del 2-9, vale 10 (para 10)
    return 10





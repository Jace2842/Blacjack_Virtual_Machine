import pygame
import re
from SimpleStack import *

# Inicializa Pygame
pygame.init()

# Inicializa el mixer de Pygame para el sonido
pygame.mixer.init()
pygame.init()


# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuración de la pantalla
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 680
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Cartas")

# Cargar la imagen de fondo
BACKGROUND_IMAGE = pygame.image.load("C:\\Users\\jesus\\Desktop\\stack virtual machine\\files\\background.jpg")

archivo_cartas = 'cartas.bj'
archivo_compilador ='comando.bj'

# Cargar musica
pygame.mixer.music.load("C:\\Users\\jesus\\Desktop\\stack virtual machine\\files\\videoplayback.wav")


pygame.mixer.music.play()
# Clase del Juego
class CardGame:
    def __init__(self):
        self.cartas = Stack(52)
        self.pila_Jugador = Stack(10)
        self.pila_Crupier = Stack(10)
        self.contadores = {'jugador': 0, 'crupier': 0}
        self.dinero = 100  # Dinero inicial
        self.apuesta = 15  # Apuesta inicial
        self.comandos = []  # Lista para almacenar comandos


    def cargar_cartas(self):
       if archivo_cartas.endswith('.bj'):
        with open(archivo_cartas) as f:
            lines = f.readlines()
        for word in lines:
            self.push = self.cartas.push(word.strip())
       else:
           print('solo acepto.bj')

    def ejecutar_comando(self, comando):
        contador_jugador = self.contadores['jugador']
        contador_crupier = self.contadores['crupier']



        if comando == "pop_alternado":
           if contador_jugador <=21 and contador_crupier<=21:
            if self.dinero < self.apuesta:
                print("No hay suficiente dinero para apostar.")
            if self.dinero >= self.apuesta:
                # Realizar pop alternado entre el jugador y el crupier
                if len(self.cartas) < 4:
                    print("No hay suficientes cartas para apostar.")
                else:
                    for i in range(2):  # Se hace dos veces, alternando
                        # Jugador toma una carta
                        carta_jugador = self.cartas.pop()
                        self.pila_Jugador.push(carta_jugador)
                        contador_jugador += obtener_valor(carta_jugador, contador_jugador)

                        # Crupier toma una carta
                        carta_crupier = self.cartas.pop()
                        self.pila_Crupier.push(carta_crupier)
                        contador_crupier += obtener_valor(carta_crupier, contador_crupier)

                    self.contadores['jugador'] = contador_jugador  # Actualizar el contador
                    self.contadores['crupier'] = contador_crupier  # Actualizar el contador


            else:
                print("caso no previsto")

        elif comando == "pop_jugador":
          if contador_jugador < 21:
           if len(self.cartas) < 1:
                print("No hay suficientes cartas para apostar.")
           else:
            carta_jugador = self.cartas.pop()
            self.pila_Jugador.push(carta_jugador)
            contador_jugador += obtener_valor(carta_jugador, contador_jugador)
            self.contadores['jugador'] = contador_jugador  # Actualizar el contador

        elif comando == "push_cartas":
            if len(self.cartas) == 0:
             self.cargar_cartas()
        elif comando == "pop_crupier":
         if len(self.cartas) < 4:
                print("No hay suficientes cartas para apostar.")
         else:

            if contador_crupier <= 17 and contador_jugador <= 21:
                for _ in range(1):
                    carta = self.cartas.pop()
                    self.pila_Crupier.push(carta)
                    contador_crupier += obtener_valor(carta, contador_crupier)

                # El crupier sigue pidiendo cartas hasta tener 17 o más
                while contador_crupier < 17 and not self.cartas.isEmpty():
                    carta = self.cartas.pop()
                    self.pila_Crupier.push(carta)
                    contador_crupier += obtener_valor(carta, contador_crupier)

                self.contadores['crupier'] = contador_crupier  # Actualizar el contador
                print(f"Después de hacer pop en la pila del crupier, contiene:\n{self.pila_Crupier}")
                print(f"El valor acumulado del Crupier es: {contador_crupier}")
            else:
                print("Por reglas el crupier no puede jugar")




        elif comando == "ganador":
            if self.contadores['jugador'] > self.contadores['crupier'] and self.contadores['jugador'] <= 21:
                print("El jugador gana.")
                self.dinero += 2 * self.apuesta  # Añadir el doble de la apuesta al dinero si el jugador gana
            elif self.contadores['crupier'] > 21 and self.contadores['jugador'] <= 21:
                print("El jugador gana, el crupier se pasó.")
                self.dinero += 2 * self.apuesta  # Añadir el doble de la apuesta al dinero si el jugador gana
            elif self.contadores['crupier'] <= 21 and self.contadores['jugador'] <= 21 and self.contadores['crupier']==self.contadores['jugador'] :
                print("Empate.")
                self.dinero = self.dinero  # Añadir el doble de la apuesta al dinero si el jugador gana
            else:
                self.dinero = self.dinero - self.apuesta
                print("El crupier gana.")
            print(f"Dinero restante del jugador: {self.dinero}")

        elif comando == "vaciar_pilas":
            self.pila_Jugador.clear()  # Vaciar la pila del jugador
            self.pila_Crupier.clear()  # Vaciar la pila del crupier
            self.contadores['jugador'] = 0  # Reiniciar el contador del jugador
            self.contadores['crupier'] = 0  # Reiniciar el contador del crupier
            print("Las pilas del jugador y del crupier han sido vaciadas.")

        elif comando == "vaciar_cartas":
            self.cartas.clear()   # Vaciar la pila de cartas
        elif comando == "swap":
            self.cartas.swap()   # Vaciar la pila de cartas

        elif comando.startswith("set_apuesta"):
        # Extraer el valor numérico del comando, asumiendo que el formato es "set_apuesta $valor"
         match = re.search(r'\$(\d+)', comando)
         if match:
            nueva_apuesta = int(match.group(1))  # Extrae el valor de la apuesta
            if nueva_apuesta > 0:
                self.apuesta = nueva_apuesta
                print(f"Apuesta actualizada a: {self.apuesta}")
            else:
                print("La apuesta debe ser un valor positivo.")
        else:
            print("Formato de apuesta inválido. Usa: set_apuesta $valor")
    def leer_comandos(self):
        """Leer comandos desde el archivo comandos.txt"""

        try:
           if archivo_compilador.endswith('.bj'):
            with open(archivo_compilador) as f:
                self.comandos = f.readlines()
            # Ejecutar cada comando leído
            for comando in self.comandos:
                comando = comando.strip()  # Eliminar saltos de línea y espacios
                self.ejecutar_comando(comando)
        except FileNotFoundError:
            print("El archivo 'comando.txt' no fue encontrado.")

    def draw(self):
        # Dibujar el fondo
        screen.blit(BACKGROUND_IMAGE, (0, 0))


        font = pygame.font.SysFont(None, 36)

        # Texto en blanco en la parte inferior izquierda
        text = font.render(f"Dinero: {self.dinero}", True, WHITE)
        screen.blit(text, (20, SCREEN_HEIGHT - 130))  # Subido de -100 a -130

        text = font.render(f"Apuesta: {self.apuesta}", True, WHITE)
        screen.blit(text, (20, SCREEN_HEIGHT - 100))  # Subido de -70 a -100

        text = font.render(f"Valor del Jugador: {self.contadores['jugador']}", True, WHITE)
        screen.blit(text, (20, SCREEN_HEIGHT - 70))  # Subido de -40 a -70

        text = font.render(f"Valor del Crupier: {self.contadores['crupier']}", True, WHITE)
        screen.blit(text, (20, SCREEN_HEIGHT - 40))  # Subido de -10 a -40

        text = font.render(f"cartas del Jugador: {self.pila_Jugador}", True, WHITE)
        screen.blit(text, (20, SCREEN_HEIGHT - 200))  # Subido de -40 a -70

        text = font.render(f"cartas del Crupier: {self.pila_Crupier}", True, WHITE)
        screen.blit(text, (20, SCREEN_HEIGHT - 170))  # Subido de -10 a -40

        pygame.display.flip()

# Función principal
def main():
    game = CardGame()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Leer comandos desde el archivo
                    game.leer_comandos()
                if event.key == pygame.K_p:  # Pop alternado
                    game.ejecutar_comando("pop_alternado")
                if event.key == pygame.K_j:  # Pop alternado
                    game.ejecutar_comando("pop_jugador")
                if event.key == pygame.K_g:  # Determinar ganador
                    game.ejecutar_comando("ganador")
                if event.key == pygame.K_v:  # Vaciar pilas
                    game.ejecutar_comando("vaciar_pilas")
                if event.key == pygame.K_l:  # Vaciar pilas
                    game.ejecutar_comando("push_cartas")
                if event.key == pygame.K_c:  # Vaciar pilas
                    game.ejecutar_comando("vaciar_cartas")
                if event.key == pygame.K_s:  # Vaciar pilas
                    game.ejecutar_comando("set_apuesta $20")

        game.draw()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

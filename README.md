# Juego de Cartas

## Descripción del Proyecto
Este proyecto implementa un juego de cartas simple utilizando Python y la biblioteca Pygame. El juego simula un entorno básico de cartas entre un jugador y un crupier. Los jugadores pueden interactuar con el juego presionando teclas para ejecutar varios comandos como robar cartas, determinar el ganador, hacer apuestas y más.

## Requisitos Previos
- **Python**: Debes tener Python 3.x instalado en tu sistema.
- **Pygame**: Necesitas instalar la biblioteca Pygame para ejecutar el juego. Para instalarla, ejecuta el siguiente comando:
  ```bash
  pip install pygame
- **SimpleStack**: Este proyecto utiliza una clase personalizada `SimpleStack` para gestionar las operaciones con las cartas. Debes importar esta clase en el archivo principal (`main`).
- **Archivos Multimedia**: 
  - `background.jpg`: Imagen de fondo.
  - `videoplayback.wav`: Música de fondo.

## Características del Programa

### Estructura Básica
- El juego utiliza Pygame para manejar los gráficos y el sonido.
- La clase `CardGame` gestiona la lógica del juego, incluyendo pilas de cartas para el jugador y el crupier, apuestas, y comandos para controlar el flujo del juego.

### Gestión de Cartas
- Se utilizan pilas (stacks) para gestionar las cartas tanto del jugador como del crupier.
- Los comandos como "pop" (retirar carta) y "push" (colocar carta) simulan la interacción con las pilas de cartas.

### Reglas del Juego
- Cada jugador (tanto el jugador humano como el crupier) intenta acercarse lo más posible a un puntaje de 21 sin pasarse, similar al juego de blackjack.
- Los jugadores pueden realizar apuestas y el crupier tiene restricciones sobre cuándo puede robar más cartas.

## Cómo Jugar

1. Ejecuta el codigo de Python:
2. usa los controles 
### Controles
Las siguientes teclas están mapeadas para comandos específicos del juego:

- **`A`**: Lee los comandos desde un archivo (`comando.bj`).
- **`P`**: Robar cartas para el jugador y el crupier de manera alternada (pop alternado).
- **`J`**: El jugador roba una carta.
- **`G`**: Determina el ganador según los valores actuales de las cartas.
- **`V`**: Vacía las pilas de cartas del jugador y del crupier.
- **`L`**: Reabastece el mazo si está vacío.
- **`C`**: Vacía toda la baraja de cartas.
- **`S`**: Establece la apuesta en $20.

# descripcon de los comandos:


## 1. `pop_alternado`
- **Descripción**: Permite que el jugador y el crupier roben cartas de manera alternada.
- **Funcionamiento**:
  - Verifica si ambos, el jugador y el crupier, tienen un puntaje menor o igual a 21.
  - Comprueba si el jugador tiene suficiente dinero para hacer la apuesta y si hay suficientes cartas disponibles.
  - Si se cumplen las condiciones, el jugador y el crupier roban dos cartas cada uno (en turnos alternos) y se actualizan sus contadores.

---

## 2. `pop_jugador`
- **Descripción**: Permite al jugador robar una carta del mazo.
- **Funcionamiento**:
  - Verifica que el contador del jugador sea menor que 21 y que haya al menos una carta disponible en el mazo.
  - Si se cumplen las condiciones, el jugador roba una carta, se suma su valor al contador del jugador y se actualiza la pila de cartas del jugador.

---

## 3. `push_cartas`
- **Descripción**: Rellena el mazo de cartas si está vacío.
- **Funcionamiento**:
  - Verifica si la pila de cartas está vacía.
  - Si es así, llama al método `cargar_cartas()` para recargar el mazo desde el archivo de cartas.

---

## 4. `pop_crupier`
- **Descripción**: Permite que el crupier robe cartas según las reglas del juego.
- **Funcionamiento**:
  - Comprueba si el crupier tiene un puntaje menor o igual a 17 y si hay suficientes cartas en el mazo.
  - El crupier toma cartas hasta que su contador alcance 17 o más, siguiendo las reglas del blackjack.
  - Se actualiza la pila de cartas del crupier y su contador.

---

## 5. `ganador`
- **Descripción**: Determina quién gana la ronda de juego.
- **Funcionamiento**:
  - Compara los puntajes del jugador y del crupier.
  - Si el jugador tiene un puntaje mayor que el crupier y no supera 21, el jugador gana.
  - Si el crupier supera 21, el jugador también gana.
  - Se manejan empates y se ajusta el dinero del jugador según los resultados.

---

## 6. `vaciar_pilas`
- **Descripción**: Vacía las pilas de cartas del jugador y del crupier.
- **Funcionamiento**:
  - Llama al método `clear()` en las pilas de cartas de ambos, el jugador y el crupier.
  - Reinicia los contadores de ambos a cero.

---

## 7. `vaciar_cartas`
- **Descripción**: Vacía toda la baraja de cartas.
- **Funcionamiento**:
  - Llama al método `clear()` en la pila de cartas, eliminando todas las cartas del mazo.

---

## 8. `swap`
- **Descripción**: Intercambia las cartas en la pila.
- **Funcionamiento**:
  - Invoca el método `swap()` de la clase de la pila de cartas.

---

## 9. `set_apuesta`
- **Descripción**: Establece una nueva apuesta para el jugador.
- **Funcionamiento**:
  - Este comando usa una expresión regular para extraer el valor de la apuesta del formato del comando, que debe ser `set_apuesta $valor`.
  - Verifica que el nuevo valor sea positivo y actualiza la apuesta actual del jugador.

---

### Flujo del Juego
- El jugador comienza con $100 y una apuesta inicial de $15.
- Al presionar las teclas, el jugador puede robar cartas, verificar al ganador y modificar la apuesta.
- El objetivo es vencer al crupier acercándose a un total de 21 puntos sin exceder ese número.


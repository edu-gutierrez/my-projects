# Tres en Raya (Tic-Tac-Toe) - Versión de Consola

Este repositorio contiene la implementación del juego clásico Tres en Raya (Tic-Tac-Toe) diseñado para ejecutarse en la terminal.

---

## Características del Juego

* **Modos de Juego:** Jugador vs Jugador y Jugador vs IA.
* **Inteligencia Artificial:** Implementación completa del algoritmo **Minimax**.
* **Entorno:** Consola.

## Sobre la IA

* **Nivel Fácil:** Movimientos aleatorios.
* **Nivel Imposible:** Algoritmo **Minimax**. La IA evalúa todos los estados futuros posibles del tablero para encontrar el mejor movimiento.

## Compilación y Ejecución

Requisitos: `g++` y `make`.

1. **Compilar (Usando el Makefile):**

    ```bash
    make
    ```

2. **Ejecutar el Juego:**

    ```bash
    ./TicTacToeUI
    ```

---

## Ejemplo de ejecución

```text
IA ha jugado en: (0, 2)
Turno de 'X'
Introduzca posicion(Fila, Columna):
   0   1   2
0  O | . | O
  -----------
1  . | X | .
  -----------
2  . | . | X
```

---

## Estructura y Documentación Técnica

La lógica de la IA y las funciones principales del juego están completamente documentadas usando el estándar **Doxygen**.

| Archivo | Contenido Principal |
| :--- | :--- |
| `main.cc` | Punto de entrada del programa. |
| `game.cc` / `game.hh` | Lógica pura del juego, manejo de tablero, y algoritmo **Minimax**. |
| `Makefile` | Reglas de compilación y enlace. |

### Enlace a la Documentación (Doxygen)

Para una vista detallada de todas las funciones, el flujo de la IA y los parámetros descargue el repositorio y acceda al archivo:

[**[Ver Documentación Técnica Completa Aquí]**](html/index.html)

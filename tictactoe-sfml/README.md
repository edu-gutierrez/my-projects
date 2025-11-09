# Tres en Raya (Tic-Tac-Toe) - Versión gráfica

Este repositorio contiene la implementación del juego clásico Tres en Raya (Tic-Tac-Toe) diseñado gráficamente.

---

## Características del Juego

* **Modos de Juego:** Jugador vs Jugador y Jugador vs IA (con 2 niveles de dificultad).
* **Inteligencia Artificial:** Implementación completa del algoritmo **Minimax**.
* **Entorno:** SFML.

## Compilación y Ejecución

1.  **Compilar (Usando el Makefile):**
    ```bash
    make
    ```

2.  **Ejecutar el Juego:**
    ```bash
    ./TicTacToeUI
    ```
---

## Estructura y Documentación Técnica

La lógica de la IA y las funciones principales del juego están completamente documentadas usando el estándar **Doxygen**.

| Archivo | Contenido Principal |
| :--- | :--- |
| `main.cc` | Punto de entrada del programa. |
| `game.cc` / `game.hh` | Lógica pura del juego y algoritmo **Minimax**. |
| `UI_game.cc` / `UI_game.hh` | Diseño de la interfaz gráfica con SFML. |
| `Makefile` | Reglas de compilación y enlace. |

### Enlace a la Documentación (Doxygen)

Para una vista detallada de todas las funciones, el flujo de la IA y los parámetros:

[**[Ver Documentación Técnica Completa Aquí]**](html/index.html)
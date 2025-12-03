# Portafolio de Proyectos Personales

Este repositorio es una colección de proyectos que he programado durante mis estudios de **Ingeniería Informática**. Mi objetivo es aplicar mis conocimientos para construir diversas aplicaciones.

## Proyectos Realizados

### 1. Blackjack Q-Learning

Agente de Reinforcement Learning autónomo que aprende la estrategia óptima de Blackjack mediante auto-juego

* **Tech Stack:** Python, Pickle.
* **Detalles:**
  * Implementación desde cero de **Q-Learning** y la **Ecuación de Bellman**.
  * La AI aprendió la estrategia por si sola (cuando doblar/plantarse/pedir).
  * Incluye modo de juego en terminal donde la AI te hace de "asesor" diciendote la mejor jugada.
* [Ir al código](./blackjack-q-learning/)

### 2. Algorithm Visualizer

Herramienta de escritorio para visualizar el comportamiento de algoritmos en tiempo real.

* **Tech Stack:** Python, PyQt, NumPy, PyQtGraph.
* **Detalles:**
  * Implementación de +20 algoritmos de ordenamiento, 5 de pathfinding y 4 de clustering.
* [Ir al código](./algorithm-visualizer)

### 3. GL-Scrapbook (Motor Gráfico Experimental)

Entorno de pruebas gráficas desde cero para entender el funcionamiento de un motor gráfico y la pipeline de renderizado.

* **Tech Stack:** C++, OpenGL, GLSL, GLM.
* **Detalles:**
  * Renderizado sin motores (no Unity/Unreal).
  * Implementación manual de shaders de iluminación (Phong) y mapeado de texturas.
  * Sistema de cámara y gestión de transformaciones en 3D.
* [Ir al código](./gl-scrapbook)

### 4. TicTacToe (Minimax AI)

Implementación dual (CLI y GUI) enfocada en la teoría de juegos.

* **Tech Stack:** C++, SFML.
* **Detalles:**
  * **Core:** Algoritmo Minimax recursivo (IA imposible de ganar).
  * **Arquitectura:** Desacoplamiento entre la lógica del juego y la interfaz, permitiendo pasar de Terminal a SFML reutilizando el backend.
* [Ir al código](./tictactoe-sfml)

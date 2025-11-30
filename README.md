# Portafolio de Proyectos Personales

Este repositorio es una colección de proyectos que he programado durante mis estudios de **Ingeniería Informática**. Mi objetivo es aplicar mis conocimientos para construir diversas aplicaciones.

## Proyectos Realizados

### 1. Algorithm Visualizer

Herramienta de escritorio para visualizar el comportamiento de algoritmos en tiempo real.

* **Tech Stack:** Python, PyQt, NumPy, PyQtGraph.
* **Detalles:**
  * Implementación de +20 algoritmos de ordenamiento, 5 de pathfinding y 4 de clustering.
* [Ir al código](./algorithm-visualizer)

### 2. GL-Scrapbook (Motor Gráfico Experimental)

Entorno de pruebas gráficas desde cero para entender el funcionamiento de un motor gráfico y la pipeline de renderizado.

* **Tech Stack:** C++, OpenGL, GLSL, GLM.
* **Detalles:**
  * Renderizado sin motores (no Unity/Unreal).
  * Implementación manual de shaders de iluminación (Phong) y mapeado de texturas.
  * Sistema de cámara y gestión de transformaciones en 3D.
* [Ir al código](./gl-scrapbook)

### 3. TicTacToe (Minimax AI)

Implementación dual (CLI y GUI) enfocada en la teoría de juegos.

* **Tech Stack:** C++, SFML.
* **Detalles:**
  * **Core:** Algoritmo Minimax recursivo (IA imposible de ganar).
  * **Arquitectura:** Desacoplamiento entre la lógica del juego y la interfaz, permitiendo pasar de Terminal a SFML reutilizando el backend.
* [Ir al código](./tictactoe-sfml)

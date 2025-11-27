# GL-Scrapbook: Motor de Iluminación Estilo Minecraft

Motor gráfico experimental 3D escrito desde cero en **C++ y OpenGL**.
El objetivo del proyecto es la implementación manual de un pipeline de renderizado, centrándose en un sistema de **iluminación Phong** con múltiples point lights y shaders personalizados GLSL.

Se utilizan assets estilo Minecraft para las pruebas de texturizado y mapeado UV.

## Preview

![Preview](Media/Gameplay.gif)

---

## Características Técnicas

### Sistema de Iluminación Avanzado

Implementación manual del modelo de reflexión Phong en los fragment shaders:

* **Múltiples Luces Puntuales:** Gestión simultánea de distintas fuentes de luz en la escena.
* **Atenuación Realista:** Cálculo de la caída de la luz con la distancia usando términos `constant`, `lineal` y `quadratic`.
* **Fuentes en la Demo:**
  * **Horno:** Luz cálida pulsante.
  * **Redstone:** Luz rojiza tenue.
  * **Linterna:** Luz acoplada a la cámara del jugador.

### Cámara y Renderizado

* **Cámara Orbital:** Sistema de cámara en tercera persona controlado mediante arrastre del ratón. Permite orbitar e inspeccionar la escena desde diferentes ángulos.
* **Texturizado:** Carga y mapeado de texturas estilo Minecraft.

### Controles

* Ratón para rotación de la cámara
* `ESC` para salir  
* `F` para encender/apagar el horno
* `C` para encender/apagar la luz de la cámara
* `V` para encender/apagar la luz de la redstone
* `-> / <-` para mover la vagoneta

---

## Dependencias

Este proyecto se construye con **CMake** y requiere las siguientes librerías:

* **OpenGL 3.3+ Core Profile**
* **GLFW** – Creación de ventana y manejo de input  
* **GLAD** – Carga de funciones OpenGL  
* **GLM** – Matemáticas 3D  
* **STB Image** – Cargar texturas e imágenes  

## Compilación

```bash
cmake .
make
./gl-scrapbook
```

---

### Texturas

Las texturas utilizadas en este proyecto son propiedad de Mojang Studios ©.
Se incluyen únicamente con fines educativos.
Si es necesario retirarlas por motivos de copyright, pueden ser eliminadas sin problema.

## Referencias y Créditos

Este proyecto fue desarrollado siguiendo los recursos educativos de [LearnOpenGL.com](https://learnopengl.com/).

* La configuración inicial de GLFW y la estructura base de la clase `Camera` siguen la metodología de sus tutoriales.
* El código ha sido adaptado y extendido para implementar la lógica específica de esta escena (iluminación de objetos específicos, gestión de inputs y shaders personalizados).

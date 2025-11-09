# Nombre del ejecutable final
TARGET = TicTacToeUI

# Archivos fuente 
SOURCES = game.cc UI_game.cc main.cc

# Archivos objeto 
OBJECTS = $(SOURCES:.cc=.o)

# Compilador y Banderas estándar de C++
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -pedantic -g

# Banderas de Inclusión 
SFML_INC = -I/usr/include

# Banderas de Enlace
SFML_LIBS = -lsfml-graphics -lsfml-window -lsfml-system

all: $(TARGET)

# Regla Principal
$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET) $(SFML_LIBS)

# Regla de Compilación:
%.o: %.cc
	$(CXX) $(CXXFLAGS) $(SFML_INC) -c $< -o $@

# Regla para Limpiar
clean:
	rm -f $(OBJECTS) $(TARGET)
	@echo "Archivos objeto (.o) y ejecutable eliminados."

# Reglaa Phony
.PHONY: all clean
#Nombre del ejecutable 
TARGET = TicTacToe_terminal

#Archivos fuente
SOURCES = game.cc main.cc

#Archivos objeto 
OBJECTS = $(SOURCES:.cc=.o)

#Compilador y Banderas estándar
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra

#Regla principal (construye el programa)
all: $(TARGET)

#Regla de enlace (combina todos los archivos objeto para crear el ejecutable final)
$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET)

#Regla de compilación (compila cada .cc a su .o)
%.o: %.cc
	$(CXX) $(CXXFLAGS) -c $< -o $@

#Regla para limpiar (elimina todos los archivos objeto y ejecutable)
clean:
	rm -f $(OBJECTS) $(TARGET)
	@echo "Archivos objeto y ejecutable eliminados."
	
#Indica que 'all' y 'clean' no son archivos sino comandos
.PHONY: all clean
/**
 * /**
 * @file UI_game.hh
 * @brief Implementación de la interfaz del juego Tres en Raya para SFML
 * 
 * Este archivo contiene todas las funciones que manejan la interfaz del juego y
 * la interacción con la pantalla. 
 */

#pragma once
#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include "game.hh"

using namespace std;

class gameUI{
    private:
    
    TicTacToe game;
    int difficulty = 1; //La dificultad por defecto es extremo.

    float windowSize = 600.0f;
    float cellSize = windowSize / 3.0f;
    sf::RenderWindow window;
    
    sf::Font font;
    sf::Text messageText; //"GANA","EMPATE".
    sf::Text instructionText; //"(click para reiniciar)".
    sf::Text menuTitleText; //Título.
    sf::Text optionPVP; //PlayervsPlayer.
    sf::Text optionPVSAI0; //PlayervsAI(facil).
    sf::Text optionPVSAI1; //PlayervsAI(extremo)

    /**
     * @brief Define el estado de la app (MENU | PLAYING).
     */
    enum class appState{
        MENU,
        PLAYING
    };

    /**
     * @brief Define el modo de juego en el que estamos (PVP | PVSAI).
     */
    enum class gameMode{
        PVP,
        PVSAI
    };

    appState currentState = appState::MENU; //El estado por defecto es el menú.
    gameMode currentMode = gameMode::PVSAI; //El modo por defecto es Jugador vs AI.

    /**
     * @brief Dibuja los cuadros de texto que hay en el menú.
     */
    void drawMenu();
    
    /**
     * @brief Decide que ocurre con los clicks que se hacen en la pantalla del menú.
     * @param x Posición x en la pantalla.
     * @param y Posición y en la pantalla.
     */
    void handleMenuClick(int x, int y);

    /**
     * @brief Inicializa todos los mensajes al inicio del programa.
     */
    void iniGraphics();
    
    /**
     * @brief Dibuja las líneas horizontales y verticales del tablero.
     */
    void drawGrid();
    
    /**
     * @brief Dibuja todas las piezas ('X' y 'O') en sus posiciones correspondientes del tablero.
     */
    void drawPieces();
    
    /**
     * @brief Decide que ocurre con los clicks en la pantalla de juego.
     * @param x Posición x en la pantalla.
     * @param y Posición y en la pantalla. 
     */
    void handleMouseClick(int x, int y);
    
    /**
     * @brief Convierte coordenadas de pantalla a coordenadas del tablero.
     * @param x Posición en el eje x en pantalla.
     * @param y Posición en el eje y en pantalla.
     * @return Posición (x, y) de la matriz.
     */
    pair<int, int> screenToGrid(int x, int y);

    public:

    /**
     * @brief Constructor por defecto.
     */
    gameUI();

    /**
     * @brief Bucle principal del programa.
     */
    void runGameLoop();
};
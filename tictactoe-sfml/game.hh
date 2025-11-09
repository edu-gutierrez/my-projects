/**
 * @file game.hh
 * @brief Implementación de la lógica del juego Tres en Raya para SFML,
 * incluye modo de Jugador vs Jugador y Jugador vs AI con 2 dificultades.
 * 
 * Este archivo contiene todas las funciones que manejan la lógica del juego y la AI. 
 */

#pragma once
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;
//Define un alias para la Matriz de Carácteres
using MC = vector<vector<char>>;

class TicTacToe{
    private:
    MC board;
    char currentPlayer; //('X' || 'O').
    bool isGameActive; //Indica si hay partida en curso.
    
    /**
    * @brief Verifica si el jugador especificado ha ganado la partida.
    * @param tab Referencia a la matriz del tablero 3x3.
    * @param player Carácter del jugador a verificar ('X' | 'O').
    * @return true si el jugador ha completado una (línea | columna | diagonal), false en caso contrario.
    */
    bool win(const MC& tab, char player) const;
    
    /**
     * @brief Verifica si el juego ha terminado en empate.
     * @param tab Referencia a la matriz del tablero 3x3.
     * @return true si el tablero está lleno y no hay ganador, false en caso contrario.
     */
    bool draw(const MC& tab) const;
    
    /**
     * @brief Evalúa la puntuación del tablero para el algoritmo minimax.
     * @param tab Referencia a la matriz del tablero 3x3.
     * @return 10 si 'O' gana, -10 si 'X' gana, 0 si hay empate o el juago continúa.
     */
    int eval(const MC& tab) const;
    
    /**
     * @brief Implementación del algoritmo Minimax para determinar la mejor jugada posible.
     * @param tab Referencia a la matriz del tablero 3x3.
     * @param isMax Booleano que indica si se busca maximizar (true para IA 'O') o minimizar (false para Jugador 'X').
     * @param depth Nivel de profundidad restante para la búsqueda.
     * @return La mejor puntuación alcanzable desde este estado del tablero.
     */
    int minimax(MC& tab, bool isMax, int depth);
    
    /**
     * @brief Devuelve una jugada válida en posición random.
     * @param tab Copia de la matriz del tablero 3x3.
     * @return un pair (fila, columna) con la jugada válida.
     */
    pair<int, int> jugadaRandAI();
    
    /**
     * @brief Determina la mejor jugada para la AI.
     * @param tab Copia de la matriz del tablero 3x3.
     * @return un pair (fila, columna) con la mejor jugada.
     */
    pair<int, int> jugadaTopAI();


    public:

    /**
     * @brief Constructor por defecto de la clase.
     */
    TicTacToe();

    /**
     * @brief Intenta hacer una jugada.
     * @param row Índice de la fila [0,2].
     * @param col Índice de la columna [0,2].
     * @return true si la jugada es válida, false en caso contrario.
     */
    bool makeMove(int row, int col); //Intenta hacer una jugada, devuelve true si es válida
    
    /**
     * @brief Comprueba si una celda específica es vacía
     * @param row Índice de la fila [0,2].
     * @param col Índice de la columna [0,2].
     * @return true si la casilla es '.', false en caso contrario.
     */
    bool isMoveValid(int row, int col) const;
    
    /**
     * @brief Devuelve el movimiento generado por la AI.
     * @param difficulty 0 si es modo fácil, 1 si es modo difícil.
     * @return El movimiento generado por la AI.
     */
    pair<int, int> getAIMove(int difficulty);

    /**
     * @brief Devuelve el estado del ganador de la partida.
     * @return 'X', 'O', 'D'(draw) o '.'(juego en curso)
     */
    char getWinner() const;
    
    /**
     * @brief Devuelve el jugador actual.
     */
    char getCurrentPlayer() const {return currentPlayer;}
    
    /**
     * @brief Devuelve el tablero.
     */
    const MC& getBoard() const {return board;}
    
    /**
     * Comprueba si hay una partida en curso.
     */
    bool isActive() const {return isGameActive;}
    
    /**
     * @brief Devuelve los parametros a sus iniciales.
     */
    void resetGame();
};
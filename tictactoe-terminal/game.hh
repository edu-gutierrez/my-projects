/**
 * @file game.hh
 * @brief Implementación del juego Tres en Raya para la terminal,
 * incluye modo de Jugador vs Jugador y Jugador vs AI con 2 dificultades.
 * 
 * Este archivo contiene todas las funciones que manejan la lógica del juego, 
 * la interacción con consola y la AI. 
 */

#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <limits>

using namespace std;
//Define un alias para la Matriz de Carácteres
using MC = vector<vector<char>>;

/**
 * @brief Inicializa el tablero con todas las celdas vacías('.').
 * @param tab Referencia a la matriz del tablero 3x3.
 * @pre La matriz 'tab' es de 3x3.
 * @post Todas las celdas de 'tab' son '.'.
 */
void ini_tablero(MC& tab);

/**
 * @brief Muestra el estado actual del tablero por la terminal.
 * @param tab Referencia a la matriz del tablero 3x3.
 * @pre La matriz 'tab' es de 3x3.
 * @post El tablero se imprime en la terminal.
 */
void mostrar_tablero(const MC& tab);

/**
 * @brief Verifica si el jugador especificado ha ganado la partida.
 * @param tab Referencia a la matriz del tablero 3x3.
 * @param player Carácter del jugador a verificar ('X' | 'O').
 * @return true si el jugador ha completado una (línea | columna | diagonal), false en caso contrario.
 */
bool win(MC& tab, char player);

/**
 * @brief Verifica si el juego ha terminado en empate.
 * @param tab Referencia a la matriz del tablero 3x3.
 * @return true si el tablero está lleno y no hay ganador, false en caso contrario.
 */
bool draw(MC& tab);

/**
 * @brief Comprueba si una celda específica está dentro de los límites y es vacía
 * @param tab Referencia a la matriz del tablero 3x3.
 * @param posi Índice de la fila [0,2].
 * @param posj Índice de la columna [0,2].
 * @return true si la posición es válida y la casilla es '.', false en caso contrario.
 */
bool jugada_posible(const MC& tab, int posi, int posj);

/**
 * @brief Solicita y valida una jugada al usuario.
 * @param tab Referencia a la matriz del tablero 3x3.
 * @param player Carácter del jugador actual ('X' | 'O').
 * @return un pair (fila, columna) con la jugada válida introducida por el usuario.
 */
pair<int, int> pedirJugada(MC& tab, char player);

/**
 * @brief Actualiza el tablero con la jugada realizada por un jugador.
 * @param tab Referencia a la matriz del tablero 3x3.
 * @param posi Índice de la fila [0,2].
 * @param posj Índice de la columna [0,2].
 * @param player Carácter del jugador actual ('X' | 'O').
 * @pre La jugada es posible.
 * @post Se actualiza tab con los valores dados.
 */
void hacer_jugada(MC& tab, int posi, int posj, char player);

/**
 * @brief Ejecuta el bucle de JugadorvsJugador.
 */
void PlayerVsPlayer();

/**
 * @brief Devuelve una jugada válida en posición random.
 * @param tab Copia de la matriz del tablero 3x3.
 * @return un pair (fila, columna) con la jugada válida.
 */
pair<int, int> jugadaRandAI(MC tab);

/**
 * @brief Evalúa la puntuación del tablero para el algoritmo minimax.
 * @param tab Referencia a la matriz del tablero 3x3.
 * @return 10 si 'O' gana, -10 si 'X' gana, 0 si hay empate o el juago continúa.
 */
int eval(MC& tab);

/**
 * @brief Implementación del algoritmo Minimax para determinar la mejor jugada posible.
 * @param tab Referencia a la matriz del tablero 3x3.
 * @param isMax Booleano que indica si se busca maximizar (true para IA 'O') o minimizar (false para Jugador 'X').
 * @param depth Nivel de profundidad restante para la búsqueda.
 * @return La mejor puntuación alcanzable desde este estado del tablero.
 */
int minimax(MC& tab, bool isMax, int depth);

/**
 * @brief Determina la mejor jugada para la AI.
 * @param tab Copia de la matriz del tablero 3x3.
 * @return un pair (fila, columna) con la mejor jugada.
 */
pair<int, int> jugadaTopAI(MC tab);

/**
 * @brief Ejecuta el bucle de JugadorvsAI.
 */
void PlayerVsAi();

/**
 * @brief Inicia el juego.
 */
void empezar_juego();
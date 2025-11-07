/**
 * @file game.cc
 * @brief Implementación de la lógica del juego Tres en Raya para SFML.
 * 
 * Este archivo contiene la definición de todas las funciones que manejan la lógica del juego y la AI. 
 */

#include "game.hh"

TicTacToe::TicTacToe() :
    board(3, vector<char>(3, '.')),
    currentPlayer('X'),
    isGameActive(true)
    {}

bool TicTacToe::win(const MC& tab, char player)const{
    for(int i = 0; i < 3; ++i){
        //Mirar 3 filas
        if(tab[i][0] == player && tab[i][1] == player && tab[i][2] == player) return true;
        //Mirar 3 columnas
        if(tab[0][i] == player && tab[1][i] == player && tab[2][i] == player) return true;
    }
    //Mirar diagonal principal
    if(tab[0][0] == player && tab[1][1] == player && tab[2][2] == player) return true;
    //Mirar diagonal secundaria
    if(tab[0][2] == player && tab[1][1] == player && tab[2][0] == player) return true;
    return false;
}

bool TicTacToe::draw(const MC& tab)const{
    if(!win(tab, 'X') && !win(tab, 'O')){
        for(int i = 0; i < 3; ++i){
            for(int j = 0; j < 3; ++j){
                if(tab[i][j] == '.') return false;
            }
        }
    }
    return true;
}

int TicTacToe::eval(const MC& tab)const{
    if(win(tab, 'O')) return 10;
    else if(win(tab, 'X')) return -10;
    return 0;
}

int TicTacToe::minimax(MC& tab, bool isMax, int depth){
    int val = eval(tab);
    //Si alguien ha ganado o se llega a la profundidas límite se termina la recursión (poda).
    if(val == 10 || val == -10 || depth == 0) return val;
    bool quedanMovs = false;
    //Comprobamos si hay casillas disponibles.
    for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
            if(tab[i][j] == '.') quedanMovs = true;
        }
    }
    //Si no quedan casillas es un empate.
    if(!quedanMovs) return 0;

    //Turno AI
    if(isMax){ 
        //Inicializamos el mejor valor con un número muy bajo (peor resultado posible para la AI).
        int mejor = -1000;
        for(int i = 0; i < 3; ++i){
            for(int j = 0; j < 3; ++j){
                if(tab[i][j] == '.'){
                    //Simulamos jugada.
                    tab[i][j] = 'O';
                    //Le pasamos el turno al minimizador (llamada recursiva).
                    mejor = max(mejor, minimax(tab, false, depth - 1));
                    //Deshacemos la jugada.
                    tab[i][j] = '.';
                }
            }
        }
        //Devuelve la mejor punuacion a la que se puede llegar.
        return mejor;

    //Turno Jugador
    }else{ 
        //Inicializamos el peor valor con un número muy alto (peor resultado posible para la AI).
        int peor = 1000;
        for(int i = 0; i < 3; ++i){
            for(int j = 0; j < 3; ++j){
                if(tab[i][j] == '.'){
                    //Simulamos jugada.
                    tab[i][j] = 'X';
                    //Le pasamos el turno al maximizador (llamada recursiva).
                    peor = min(peor, minimax(tab, true, depth - 1));
                    //Deshacemos jugada
                    tab[i][j] = '.';
                }
            }
        }
        //Devuelve la peor puntuación a la que se puede llegar.
        return peor;
    }
}
   
pair<int, int> TicTacToe::jugadaRandAI(){
    bool valid = false;
    int i, j;
    while(!valid){
        i = rand() % 3;
        j = rand() % 3;
        valid = (board[i][j] == '.');
    }
    return make_pair(i, j);
}

pair<int, int> TicTacToe::jugadaTopAI(){
    //Se inicializa el mejor valor como el peor resultado posible para la AI.
    int bestVal = -1000;
    //El mejor movimiento es nulo.
    pair<int, int> bestMove = {-1, -1};

    for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
            if(board[i][j] == '.'){
                //Simulamos jugada
                board[i][j] = 'O';
                //Calculamos el valor óptimo.
                int valMove = minimax(board, false, 9);
                //Deshacemos jugada.
                board[i][j] = '.';
                //Comparamos si el valor es mejor a lo que ya teníamos.
                if(valMove > bestVal){
                    bestVal = valMove;
                    bestMove = {i, j};
                }
            }
        }
    }
    return bestMove;
}

bool TicTacToe::makeMove(int row, int col){
    if(!isGameActive || !isMoveValid(row, col)) return false;
    board[row][col] = currentPlayer;
    char winner = getWinner();
    if(winner != '.'){
        isGameActive = false;
    }else{
        if(currentPlayer == 'X') currentPlayer = 'O';
        else currentPlayer = 'X';
    }
    return true;
}

bool TicTacToe::isMoveValid(int row, int col) const{
    if(board[row][col] == '.') return true;
    return false;
}

pair<int, int> TicTacToe::getAIMove(int difficulty){ //difficulty = 0 (Easy)
    if(difficulty == 0) return jugadaRandAI();
    return jugadaTopAI();
}

char TicTacToe::getWinner() const{
    if(win(board, 'X')) return 'X';
    else if(win(board, 'O')) return 'O';
    else if(draw(board)) return 'D';
    return '.';
} 

void TicTacToe::resetGame(){
    for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
            board[i][j] = '.';
        }
    }
    isGameActive = true;
    currentPlayer = 'X';
}

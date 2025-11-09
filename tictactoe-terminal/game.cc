/**
 * @file game.cc
 * @brief Implementación del juego Tres en Raya para la terminal.
 * 
 * Este archivo contiene la definición de todas las funciones que manejan la lógica del juego, 
 * la interacción con consola y la AI. 
 */

#include "game.hh"

void ini_tablero(MC& tab){
    for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
            tab[i][j] = '.';
        }
    }
}

void mostrar_tablero(const MC& tab){
    cout << "   0   1   2" << endl;
    for(int i = 0; i < 3; ++i){
        cout << i << "  ";
        for(int j = 0; j < 3; ++j){
            cout << tab[i][j];
            if(j != 2) cout << " | ";
        }
        cout << endl;
        if(i != 2) cout << "  -----------" << endl;
    }
}

bool win(MC& tab, char player){
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

bool draw(MC& tab){
    if(!win(tab, 'X') && !win(tab, 'O')){
        for(int i = 0; i < 3; ++i){
            for(int j = 0; j < 3; ++j){
                if(tab[i][j] == '.') return false;
            }
        }
    }
    return true;
}

bool jugada_posible(const MC& tab, int posi, int posj){
    if(posi > 2 || posi < 0 || posj > 2 || posj < 0 || tab[posi][posj] != '.') return false;
    return true;
}

pair<int, int> pedirJugada(MC& tab, char player){
    bool valid = false;
    int posi, posj;
    while(!valid){
        cout << "Turno de '" << player << "'" << endl;
        cout << "Introduzca posicion(Fila, Columna):" << endl;
        mostrar_tablero(tab);
        cin >> posi >> posj;

        if(cin.fail()){
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Entrada no valida. Introduce dos numeros entre 0 y 2." << endl;
            continue;
        }

        if(jugada_posible(tab, posi, posj)) valid = true;
        else cout << "Jugada no posible, escoja de nuevo:" << endl;
    }
    return{posi, posj};
}

void hacer_jugada(MC& tab, int posi, int posj, char player){
    tab[posi][posj] = player;
}

void PlayerVsPlayer(){
    bool turnoP1 = true;
    int numTurno = 1;
    MC tab = {{'.', '.', '.'}, {'.', '.', '.'}, {'.', '.', '.'}};
    ini_tablero(tab);
    bool ganado = false;

    while(numTurno != 10 && !ganado){
        char player;
        if(turnoP1) player = 'X';
        else player = 'O';
        
        pair<int, int> move = pedirJugada(tab, player);
        hacer_jugada(tab, move.first, move.second, player);

        if(win(tab, player)){
            mostrar_tablero(tab);
            cout << "Jugador '" << player << "' gana!" << endl;
            ganado = true;
        }
        ++numTurno;
        turnoP1 = !turnoP1;
    }
    if(draw(tab)) cout << "EMPATE!" << endl;
}

pair<int, int> jugadaRandAI(MC tab){
    bool valid = false;
    int i, j;
    while(!valid){
        i = rand() % 3;
        j = rand() % 3;
        valid = jugada_posible(tab, i, j);
    }
    return make_pair(i, j);
}

int eval(MC& tab){
    if(win(tab, 'O')) return 10;
    else if(win(tab, 'X')) return -10;
    return 0;
}

int minimax(MC& tab, bool isMax, int depth){
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

pair<int, int> jugadaTopAI(MC tab){
    //Se inicializa el mejor valor como el peor resultado posible para la AI.
    int bestVal = -1000;
    //El mejor movimiento es nulo.
    pair<int, int> bestMove = {-1, -1};

    for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
            if(tab[i][j] == '.'){
                //Simulamos jugada
                tab[i][j] = 'O';
                //Calculamos el valor óptimo.
                int valMove = minimax(tab, false, 9);
                //Deshacemos jugada.
                tab[i][j] = '.';
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

void PlayerVsAi(){
    int difficulty = 0;
    while(difficulty != 1 && difficulty != 2){
        cout << "Selecciona nivel de dificultad:" << endl << "Facil(1)" << endl << "Extremo(2)" << endl;
        cin >> difficulty;
    }

    bool turnoJugador = true;
    int numTurno = 1;
    MC tab = {{'.', '.', '.'}, {'.', '.', '.'}, {'.', '.', '.'}};;
    ini_tablero(tab);
    bool ganado = false;

    while(numTurno != 10 && !ganado){
        char player;
        if(turnoJugador){
            player = 'X';
            pair<int, int> move = pedirJugada(tab, player);
            hacer_jugada(tab, move.first, move.second, player);
            if(win(tab, player)){
                mostrar_tablero(tab);
                cout << "Jugador '" << player << "' gana!" << endl;
                ganado = true;
            }

        }else{
            player = 'O';
            pair<int,int> mov;

            if(difficulty == 1) mov = jugadaRandAI(tab);
            else mov = jugadaTopAI(tab);

            int posi = mov.first, posj = mov.second;
            hacer_jugada(tab, posi, posj, player);
            cout << "IA ha jugado en: (" << posi << ", " << posj << ")" << endl;
            
            if(win(tab, player)){
                mostrar_tablero(tab);
                cout << "Jugador '" << player << "' gana!" << endl;
                ganado = true;
            }
        }
        
        ++numTurno;
        turnoJugador = !turnoJugador;
    }
    if(draw(tab)) cout << "EMPATE!" << endl;
}

void empezar_juego(){
    int modo = 0;
    cout << "Bienvenido al 3 en raya" << endl;
    while(modo != 1 && modo != 2){
        cout << "Selecciona modo de juego:" << endl << "Jugador contra IA(1)" << endl << "Jugador contra jugador(2)" << endl;
        cin >> modo;
    }
    if(modo == 1) PlayerVsAi();
    else if(modo == 2) PlayerVsPlayer();
}

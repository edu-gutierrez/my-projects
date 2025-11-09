/**
 * @file main.cc
 * @brief Ejecutor del Tres en Raya para SFML.
 */

#include "UI_game.hh"
#include "game.hh"
#include <cstdlib>
#include <ctime>

int main(){
    //Inicializamos semilla random
    srand(time(0));

    gameUI ui;
    ui.runGameLoop();
    return 0;
}
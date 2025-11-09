/**
 * @file UI_game.cc
 * @brief Implementación de la interfaz del juego Tres en Raya para SFML
 * 
 * Este archivo contiene la definición de todas las funciones que manejan la interfaz del juego y
 * la interacción con la pantalla. 
 */

#include "UI_game.hh"
#include <iostream>
#include <math.h>

gameUI::gameUI()
    //inicializamos la ventana convirtiendo los floats a u_int
    : game(),
      difficulty(1),
      window(sf::VideoMode(static_cast<unsigned int>(windowSize), 
                           static_cast<unsigned int>(windowSize)), 
                           "Tres en Raya", //Nombre de la ventana
                           sf::Style::Titlebar | sf::Style::Close)

{
    iniGraphics();
}

void gameUI::iniGraphics(){
    //Cargamos la fuente.
    if(!font.loadFromFile("arial.ttf")){
        cerr << "ERROR: No se pudo abrir el archivo 'arial.ttf'." << endl;
        exit(1);
    }
    messageText.setFont(font);
    messageText.setCharacterSize(60);
    messageText.setFillColor(sf::Color::Black);

    instructionText = messageText;
    instructionText.setCharacterSize(30);

    menuTitleText = instructionText;
    menuTitleText.setCharacterSize(70);
    menuTitleText.setString("Tres en Raya");

    optionPVP = menuTitleText;
    optionPVP.setCharacterSize(40);
    optionPVP.setString("1-Jugador vs Jugador");

    optionPVSAI0 = optionPVP;
    optionPVSAI0.setString("2-Jugador vs IA (Facil)");

    optionPVSAI1 = optionPVP;
    optionPVSAI1.setString("3-Jugador vs IA (Extremo)");
}

void gameUI::drawGrid(){
    sf::RectangleShape line;
    //Grosor de la linea
    const float lineThickness = 5.0f;
    //Color gris
    sf::Color grey = sf::Color(128,128,128);
    line.setFillColor(grey);
    //Linea vertical
    line.setSize(sf::Vector2f(lineThickness, windowSize));
    //Dibujamos las 2 verticales
    for(int i = 0; i < 2; ++i){
        float posX = (i+1) * cellSize;
        line.setPosition(posX - lineThickness/2, 0.0f);
        window.draw(line);
    }
    //Linea horizontal
    line.setSize(sf::Vector2f(windowSize, lineThickness));
    //Dibujamos las 2 horizontales
    for(int i = 0; i < 2; ++i){
        float posY = (i+1) * cellSize;
        line.setPosition(0.0f, posY - lineThickness/2);
        window.draw(line);
    }
}

void gameUI::drawPieces(){
    const MC& board = game.getBoard();
    for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
            if(board[i][j] == 'X'){
                sf::RectangleShape line1, line2;
                const float lineThickness = 5.0f;
                line1.setFillColor(sf::Color::Blue);
                line1.setSize(sf::Vector2f(cellSize/1.5f, lineThickness));
                //Centramos la linea en el cuadrado correspondiente                    
                line1.setOrigin((cellSize/1.5f)/2.0f , lineThickness/2.0f);
                line1.setPosition(cellSize*j + cellSize/2, cellSize*i + cellSize/2);

                line2 = line1;

                line1.rotate(45.0f);
                window.draw(line1);
                line2.rotate(135.0f);
                window.draw(line2);
            }else if(board[i][j] == 'O'){
                sf::CircleShape circle; 
                const float circleThickness = 5.0f;
                const float radius = cellSize/3;
                circle.setFillColor(sf::Color::White);
                circle.setRadius(radius);
                circle.setOutlineThickness(circleThickness);
                circle.setOutlineColor(sf::Color::Red);
                circle.setPosition(cellSize*j - radius + cellSize/2, cellSize*i - radius + cellSize/2);
                window.draw(circle);
            }
        }
    }
}

void gameUI::handleMouseClick(int x, int y){
    if(!game.isActive()){
        game.resetGame();
        return;
    }
    if(currentMode == gameMode::PVSAI && game.getCurrentPlayer() == 'O') return;
    
    //Buscamos donde hizo el click y hacemos el movimiento
    pair<int, int> posGrid = screenToGrid(x, y);
    game.makeMove(posGrid.first, posGrid.second);
}

pair<int, int> gameUI::screenToGrid(int x, int y){
    pair<int, int> coordinates;
    coordinates = make_pair(floor(y/cellSize), floor(x/cellSize));
    return coordinates;
}

void gameUI::drawMenu(){
    //Título
    sf::FloatRect boundsTitle = menuTitleText.getLocalBounds();
    menuTitleText.setOrigin(boundsTitle.left + boundsTitle.width / 2.0f,
                            boundsTitle.top + boundsTitle.height / 2.0f);
    menuTitleText.setPosition(windowSize / 2.0f, windowSize / 2.0f - 150.0f);
    window.draw(menuTitleText);

    // Opción PvP
    sf::FloatRect boundsPVP = optionPVP.getLocalBounds();
    optionPVP.setOrigin(boundsPVP.left + boundsPVP.width / 2.0f,
                        boundsPVP.top + boundsPVP.height / 2.0f);
    optionPVP.setPosition(windowSize / 2.0f, windowSize / 2.0f);
    window.draw(optionPVP);

    // Opción PVSAI0 (fácil)
    sf::FloatRect boundsPVSAI0 = optionPVSAI0.getLocalBounds();
    optionPVSAI0.setOrigin(boundsPVSAI0.left + boundsPVSAI0.width / 2.0f,
                         boundsPVSAI0.top + boundsPVSAI0.height / 2.0f);
    optionPVSAI0.setPosition(windowSize / 2.0f, windowSize / 2.0f + 80.0f);
    window.draw(optionPVSAI0);

    // Opción PVSAI1 (difícil)
    sf::FloatRect boundsPVSAI1 = optionPVSAI1.getLocalBounds();
    optionPVSAI1.setOrigin(boundsPVSAI1.left + boundsPVSAI1.width / 2.0f,
                               boundsPVSAI1.top + boundsPVSAI1.height / 2.0f);
    optionPVSAI1.setPosition(windowSize / 2.0f, windowSize / 2.0f + 160.0f);
    window.draw(optionPVSAI1);
}

void gameUI::handleMenuClick(int x, int y){
    if (currentState != appState::MENU) return;
    sf::Vector2f clickPos(static_cast<float>(x), static_cast<float>(y));

    //Jugador VS Jugador
    if (optionPVP.getGlobalBounds().contains(clickPos)) {
        currentMode = gameMode::PVP;
        currentState = appState::PLAYING;
        optionPVP.setFillColor(sf::Color::Blue); 
        optionPVSAI0.setFillColor(sf::Color::Black);
        optionPVSAI1.setFillColor(sf::Color::Black);
        game.resetGame();
        return;
    }

    //Jugador VS AI (Fácil)
    if (optionPVSAI0.getGlobalBounds().contains(clickPos)) {
        currentMode = gameMode::PVSAI;
        difficulty = 0; 
        optionPVSAI0.setFillColor(sf::Color::Blue); 
        optionPVSAI1.setFillColor(sf::Color::Black);
        optionPVP.setFillColor(sf::Color::Black); 
        currentState = appState::PLAYING;
        game.resetGame();
        return;
    }
    
    //Jugador VS AI (Extremo)
    if (optionPVSAI1.getGlobalBounds().contains(clickPos)) {
        currentMode = gameMode::PVSAI;
        difficulty = 1; 
        optionPVSAI1.setFillColor(sf::Color::Blue); 
        optionPVSAI0.setFillColor(sf::Color::Black);
        optionPVP.setFillColor(sf::Color::Black); 
        currentState = appState::PLAYING;
        game.resetGame();
        return;
    }
}

void gameUI::runGameLoop() {
    sf::Event event;

    while (window.isOpen()) {
        
        //Procesamiento de eventos.
        while (window.pollEvent(event)) {
            //Cerrar ventana.
            if (event.type == sf::Event::Closed) {
                window.close();
            }
            //Click del ratón.
            if (event.type == sf::Event::MouseButtonPressed) {
                if (event.mouseButton.button == sf::Mouse::Left) {
                    if(currentState == appState::MENU){
                        handleMenuClick(event.mouseButton.x, event.mouseButton.y);
                    }else if(currentState == appState::PLAYING){
                        handleMouseClick(event.mouseButton.x, event.mouseButton.y);
                    }
                }else if(event.mouseButton.button == sf::Mouse::Right){
                    currentState = appState::MENU;
                    currentMode = gameMode::PVP;
                    game.resetGame();
                }
            }
        }

        //Turno AI
        if (game.isActive() && game.getCurrentPlayer() == 'O' && currentState == appState::PLAYING && currentMode == gameMode::PVSAI){
            std::pair<int, int> move = game.getAIMove(difficulty);
            game.makeMove(move.first, move.second);
        }

        //Dibujo
        window.clear(sf::Color::White); 
        
        if(currentState == appState::MENU){
            drawMenu();
        }else if(currentState == appState::PLAYING){
            drawGrid();
            drawPieces();
        
            if (!game.isActive()) {
                char winner = game.getWinner();
                string msgWinner;
                
                if (winner == 'D') {
                    msgWinner = "EMPATE";
                } else {
                    msgWinner = "GANA '" + string(1, winner) + "'";
                }
                //MENSAJE PRINCIPAL
                messageText.setString(msgWinner);
                sf::FloatRect boundsWinner = messageText.getLocalBounds();
                messageText.setOrigin(boundsWinner.left + boundsWinner.width / 2.0f,
                                    boundsWinner.top + boundsWinner.height / 2.0f);
                //Hacemos que esté 40 píxeles por encima del centro
                messageText.setPosition(windowSize / 2.0f, windowSize / 2.0f - 40.0f);
                window.draw(messageText);
                
                //MENSAJE DE INSTRUCCIÓN
                instructionText.setString("(Click izquierdo para reiniciar)\n(Click derecho para volver al menu)");
                sf::FloatRect boundsInst = instructionText.getLocalBounds();
                instructionText.setOrigin(boundsInst.left + boundsInst.width / 2.0f,
                                        boundsInst.top + boundsInst.height / 2.0f);
                //Hacemos que este 40 píxeles por debajo del centro
                instructionText.setPosition(windowSize / 2.0f, windowSize / 2.0f + 40.0f);
                window.draw(instructionText);
            }    
        }
        window.display();
    }
}
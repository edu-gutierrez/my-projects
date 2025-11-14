#pragma once
#include "OpenGL/functions.hh"

struct Textures{
    unsigned int stone;
    unsigned int redstoneOre;
    unsigned int ironBlock;
    unsigned int diamondBlock;
    unsigned int oakPlanks;
    unsigned int cobbledDeepslate;
    unsigned int furnaceTop;
    unsigned int furnaceSide;
    unsigned int furnaceFront;
    unsigned int furnaceFrontOn;
    unsigned int coalOre;
    unsigned int diamondOre;
    unsigned int emeraldOre;
    unsigned int goldOre;
    unsigned int ironOre;
    unsigned int cobweb;
    unsigned int tntBottom;
    unsigned int tntSide;
    unsigned int tntTop;
    unsigned int goldBlock;
    unsigned int emeraldBlock;
};

void loadAllTextures(Textures &t);

void unloadAllTextures(Textures &t);
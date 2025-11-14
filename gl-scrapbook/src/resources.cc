#include "resources.hh"

void loadAllTextures(Textures &t){
    t.stone = loadTextureRGB("Resources/Stone.png");
    t.redstoneOre = loadTextureRGB("Resources/Redstone_Ore.png");
    t.ironBlock = loadTextureRGB("Resources/iron_block.png");
    t.diamondBlock = loadTextureRGB("Resources/Diamond_Block.png");
    t.oakPlanks = loadTextureRGB("Resources/oak_planks.png");
    t.cobbledDeepslate = loadTextureRGB("Resources/cobbled_deepslate.png");
    t.furnaceTop = loadTextureRGB("Resources/furnace_top.png");
    t.furnaceSide = loadTextureRGB("Resources/furnace_side.png");
    t.furnaceFront = loadTextureRGB("Resources/furnace_front.png");
    t.furnaceFrontOn = loadTextureRGB("Resources/furnace_front_on.png");
    t.coalOre = loadTextureRGB("Resources/coal_ore.png");
    t.diamondOre = loadTextureRGB("Resources/diamond_ore.png");
    t.emeraldOre = loadTextureRGB("Resources/emerald_ore.png");
    t.goldOre = loadTextureRGB("Resources/gold_ore.png");
    t.ironOre = loadTextureRGB("Resources/iron_ore.png");
    t.tntBottom = loadTextureRGB("Resources/tnt_bottom.png");
    t.tntSide = loadTextureRGB("Resources/tnt_side.png");
    t.tntTop = loadTextureRGB("Resources/tnt_top.png");
    t.goldBlock = loadTextureRGB("Resources/gold_block.png");
    t.emeraldBlock = loadTextureRGB("Resources/emerald_block.png");
}

void unloadAllTextures(Textures &t){
    glDeleteTextures(1, &t.stone);
    glDeleteTextures(1, &t.redstoneOre);
    glDeleteTextures(1, &t.ironBlock);
    glDeleteTextures(1, &t.diamondBlock);
    glDeleteTextures(1, &t.oakPlanks);
    glDeleteTextures(1, &t.cobbledDeepslate);
    glDeleteTextures(1, &t.furnaceTop);
    glDeleteTextures(1, &t.furnaceSide);
    glDeleteTextures(1, &t.furnaceFront);
    glDeleteTextures(1, &t.furnaceFrontOn);
    glDeleteTextures(1, &t.coalOre);
    glDeleteTextures(1, &t.diamondOre);
    glDeleteTextures(1, &t.emeraldOre);
    glDeleteTextures(1, &t.goldOre);
    glDeleteTextures(1, &t.ironOre);
    glDeleteTextures(1, &t.tntBottom);
    glDeleteTextures(1, &t.tntSide);
    glDeleteTextures(1, &t.tntTop);
    glDeleteTextures(1, &t.goldBlock);
    glDeleteTextures(1, &t.emeraldBlock);
}
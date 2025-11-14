#pragma once
#include "OpenGL/shader.hh"
#include "resources.hh"

void drawBlock(const Shader &shader, unsigned int VAO, const glm::vec3 &pos, unsigned int textureID, const glm::vec3 &scale);

void drawEnvironment(const Shader &shader, unsigned int VAO, const Textures &t);

void drawRail(const Shader &shader, unsigned int VAO, const Textures &t);

void drawMinecart(const Shader &shader, unsigned int VAO, float x, const Textures &t);

void drawRedstoneOres(const Shader &shader, unsigned int VAO, const Textures &t);

void drawOres(const Shader &shader, unsigned int VAO, const Textures &t);

void drawFurnaceBlock(const Shader &shader, unsigned int VAO, const Textures &t);

void drawShinyBlocks(const Shader &shader, unsigned int VAO, const Textures &t);

void drawTnt(const Shader &shader, unsigned int VAO, const Textures &t);

void drawObjects(const Shader &shader, unsigned int VAO, const Textures &t);
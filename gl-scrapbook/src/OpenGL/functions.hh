#pragma once
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include "stb_image.h"

unsigned int loadTextureRGB(const char* name);

unsigned int loadTextureRGBA(const char* name);

void framebuffer_size_callback(GLFWwindow *window, int width, int height);

unsigned int getVAO(const float *vertices, size_t size);

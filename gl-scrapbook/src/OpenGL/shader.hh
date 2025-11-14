#ifndef SHADER_HH
#define SHADER_HH

#include <glad/glad.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

using namespace std;

class Shader{
    public:

    unsigned int ID;
    Shader(const char* vertexPath, const char* fragmentPath);

    void use();
    void setBool(const string &name, bool value) const;
    void setInt(const string &name, int value) const;
    void setFloat(const string &name, float value) const;
    void setMat4(const string &name, glm::mat4 matrix) const;
    void setVec4(const string &name, glm::vec4 vector) const;
    void setVec3(const string &name, glm::vec3 vector) const;
    void setVec2(const string &name, glm::vec2 vector) const;

};
#endif
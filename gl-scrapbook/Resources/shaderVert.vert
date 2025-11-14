#version 330 core
layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoord;

out vec3 N;
out vec3 N_w;
out vec3 P_eye;
out vec2 TexCoord;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main()
{
    mat3 normalMatrix_v = transpose(inverse(mat3(viewMatrix*modelMatrix)));
    N_w = normalize(transpose(inverse(mat3(modelMatrix))) * normal);
    N = normalize(normalMatrix_v * normal);
    P_eye = (viewMatrix*modelMatrix*vec4(vertex, 1.0)).xyz;
    gl_Position = projectionMatrix*viewMatrix*modelMatrix*vec4(vertex, 1.0f);
    TexCoord = texCoord;
}
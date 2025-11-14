#include "functions.hh"
using namespace std;

unsigned int loadTextureRGB(const char* name){
    unsigned int texture;
	glGenTextures(1, &texture);
	glBindTexture(GL_TEXTURE_2D, texture);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	int width, height, nrChannels;
	stbi_set_flip_vertically_on_load(true); 
	unsigned char *data = stbi_load(name, &width, &height, &nrChannels, 0);
	if(data){
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
		glGenerateMipmap(GL_TEXTURE_2D);
	}else{
		cout << "No se pudo cargar la textura" << endl;
	}
	stbi_image_free(data);
    return texture;
}

unsigned int loadTextureRGBA(const char* name){
        unsigned int texture;
	glGenTextures(1, &texture);
	glBindTexture(GL_TEXTURE_2D, texture);
	int width, height, nrChannels;
	stbi_set_flip_vertically_on_load(true); 
	unsigned char *data = stbi_load(name, &width, &height, &nrChannels, 0);
	if(data){
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
		glGenerateMipmap(GL_TEXTURE_2D);
	}else{
		cout << "No se pudo cargar la textura" << endl;
	}
	stbi_image_free(data);
    return texture;
}

void framebuffer_size_callback(GLFWwindow *window, int width, int height){
	glViewport(0, 0, width, height);
}

unsigned int getVAO(const float *vertices, size_t size){
	unsigned int VBO, VAO;
	
	glGenVertexArrays(1, &VAO);  
	glGenBuffers(1, &VBO);  

	glBindVertexArray(VAO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);  
	glBufferData(GL_ARRAY_BUFFER, size, vertices, GL_STATIC_DRAW);

	//Posicion de vertices
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
	glEnableVertexAttribArray(0);
	//Normales
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(3*sizeof(float)));
	glEnableVertexAttribArray(1);
	//Coordenadas de textura
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(6*sizeof(float)));
	glEnableVertexAttribArray(2);
	//Limpieza
	glBindBuffer(GL_ARRAY_BUFFER, 0); 
    glBindVertexArray(0);
	
	return VAO;
}

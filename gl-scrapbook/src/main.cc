#include "OpenGL/functions.hh"
#include "OpenGL/camera.hh"
#include "OpenGL/shader.hh"
#include "resources.hh"
#include "render.hh"

const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

Camera camera(glm::vec3(0.0f, 1.5f, 0.0f));
float lastX = SCR_WIDTH / 2.0f;
float lastY = SCR_HEIGHT / 2.0f;
bool firstMouse = true;
bool leftMouseButtonPressed = false;

void mouseCallback(GLFWwindow *window, double xpos, double ypos);
void mouseButtonCallback(GLFWwindow *window, int button, int action, int mods);

bool drawFurnace = false, furnaceOn = false, fKeyPressed = false;
bool camLightOn = false, cKeyPressed = false;;
bool redstoneLightOn = false, vKeyPressed = false;
float minecartOffset = 2.25f;
void processInput(GLFWwindow *window, Shader &shader);
void initializeShader(const Shader &shader);

float cubeVertices[] = {
		// positions        //normals        // texture coords
		//-Z
		-0.5f, -0.5f, -0.5f, 0.0, 0.0, -1.0, 0.0f, 0.0f,
		0.5f, -0.5f, -0.5f,  0.0, 0.0, -1.0, 1.0f, 0.0f,
		0.5f,  0.5f, -0.5f,  0.0, 0.0, -1.0, 1.0f, 1.0f,
		0.5f,  0.5f, -0.5f,  0.0, 0.0, -1.0, 1.0f, 1.0f,
		-0.5f,  0.5f, -0.5f, 0.0, 0.0, -1.0, 0.0f, 1.0f,
		-0.5f, -0.5f, -0.5f, 0.0, 0.0, -1.0, 0.0f, 0.0f,
		//+Z
		-0.5f, -0.5f,  0.5f, 0.0, 0.0, 1.0, 0.0f, 0.0f,
		0.5f, -0.5f,  0.5f,  0.0, 0.0, 1.0, 1.0f, 0.0f,
		0.5f,  0.5f,  0.5f,  0.0, 0.0, 1.0, 1.0f, 1.0f,
		0.5f,  0.5f,  0.5f,  0.0, 0.0, 1.0, 1.0f, 1.0f,
		-0.5f,  0.5f,  0.5f, 0.0, 0.0, 1.0, 0.0f, 1.0f,
		-0.5f, -0.5f,  0.5f, 0.0, 0.0, 1.0, 0.0f, 0.0f,
		//-X
		-0.5f,  0.5f,  0.5f, -1.0, 0.0, 0.0, 0.0f, 1.0f,
		-0.5f,  0.5f, -0.5f, -1.0, 0.0, 0.0, 1.0f, 1.0f,
		-0.5f, -0.5f, -0.5f, -1.0, 0.0, 0.0, 1.0f, 0.0f,
		-0.5f, -0.5f, -0.5f, -1.0, 0.0, 0.0, 1.0f, 0.0f,
		-0.5f, -0.5f,  0.5f, -1.0, 0.0, 0.0, 0.0f, 0.0f,
		-0.5f,  0.5f,  0.5f, -1.0, 0.0, 0.0, 0.0f, 1.0f,
		//+X
		0.5f,  0.5f,  0.5f, 1.0, 0.0, 0.0, 0.0f, 1.0f,
		0.5f,  0.5f, -0.5f, 1.0, 0.0, 0.0, 1.0f, 1.0f,
		0.5f, -0.5f, -0.5f, 1.0, 0.0, 0.0, 1.0f, 0.0f,
		0.5f, -0.5f, -0.5f, 1.0, 0.0, 0.0, 1.0f, 0.0f,
		0.5f, -0.5f,  0.5f, 1.0, 0.0, 0.0, 0.0f, 0.0f,
		0.5f,  0.5f,  0.5f, 1.0, 0.0, 0.0, 0.0f, 1.0f,
		//-Y
		-0.5f, -0.5f, -0.5f, 0.0, -1.0, 0.0, 0.0f, 1.0f,
		0.5f, -0.5f, -0.5f,  0.0, -1.0, 0.0, 1.0f, 1.0f,
		0.5f, -0.5f,  0.5f,  0.0, -1.0, 0.0, 1.0f, 0.0f,
		0.5f, -0.5f,  0.5f,  0.0, -1.0, 0.0, 1.0f, 0.0f,
		-0.5f, -0.5f,  0.5f, 0.0, -1.0, 0.0, 0.0f, 0.0f,
		-0.5f, -0.5f, -0.5f, 0.0, -1.0, 0.0, 0.0f, 1.0f,
		//+Y
		-0.5f,  0.5f, -0.5f, 0.0, 1.0, 0.0, 0.0f, 1.0f,
		0.5f,  0.5f, -0.5f,  0.0, 1.0, 0.0, 1.0f, 1.0f,
		0.5f,  0.5f,  0.5f,  0.0, 1.0, 0.0, 1.0f, 0.0f,
		0.5f,  0.5f,  0.5f,  0.0, 1.0, 0.0, 1.0f, 0.0f,
		-0.5f,  0.5f,  0.5f, 0.0, 1.0, 0.0, 0.0f, 0.0f,
		-0.5f,  0.5f, -0.5f, 0.0, 1.0, 0.0, 0.0f, 1.0f
	};

int main(){
  	glfwInit(); 
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);	

	GLFWwindow* window = glfwCreateWindow(800, 600, "gl-scrapbook", NULL, NULL);
	if (window == NULL)
	{
		std::cout << "Failed to create GLFW window" << std::endl;
		glfwTerminate();
		return -1;
	}
	glfwMakeContextCurrent(window);
	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);  

	glfwSetCursorPosCallback(window, mouseCallback);
	glfwSetMouseButtonCallback(window, mouseButtonCallback);

	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)){
		std::cout << "Failed to initialize GLAD" << std::endl;
		return -1;
	}   

	glEnable(GL_DEPTH_TEST); 

	Shader Shader("Resources/shaderVert.vert", "Resources/shaderFrag.frag");
	Shader.use();
	initializeShader(Shader);

	unsigned int VAOcubes = getVAO(cubeVertices, sizeof(cubeVertices));
	
	Textures textures;
	loadAllTextures(textures);

	glm::vec3 lightPositionsWCS[4] = {
		glm::vec3(-1.0f, 0.5f, 0.0f),
		glm::vec3(1.0f, 0.5f, 1.0f),
		glm::vec3(-1.0f, 1.0f, -1.0f),
		glm::vec3(0.0f, 1.0f, 0.0f),
	};
	glfwSwapInterval(1);

	while(!glfwWindowShouldClose(window)){

		processInput(window, Shader);

		glClearColor(0.1f, 0.1f, 0.1f, 1.0f);		
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		
		Shader.use();

		glm::mat4 view = camera.GetViewMatrix();
		Shader.setMat4("viewMatrix", view);
		lightPositionsWCS[3] = camera.position;

		for(int i = 0; i < 4; ++i) {
			glm::vec3 lightPosVCS = glm::vec3(view * glm::vec4(lightPositionsWCS[i], 1.0f));
			std::string name = "pointLights[" + std::to_string(i) + "].position";
			Shader.setVec3(name.c_str(), lightPosVCS);
		}

		glm::mat4 proj = glm::mat4(1.0);
		proj = glm::perspective(glm::radians(45.0f), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
		Shader.setMat4("projectionMatrix", proj);

		glBindVertexArray(VAOcubes);
		glActiveTexture(GL_TEXTURE0);
		drawOres(Shader, VAOcubes, textures);
		drawEnvironment(Shader, VAOcubes, textures);
		drawObjects(Shader, VAOcubes, textures);
		drawMinecart(Shader, VAOcubes, minecartOffset, textures);

		glBindVertexArray(0);

		glfwSwapBuffers(window);
		glfwPollEvents();    
	}
	unloadAllTextures(textures);
	glfwTerminate();
    return 0;
}

void initializeShader(const Shader &shader){
	shader.setInt("texture0", 0);
	shader.setInt("texture1", 1);
	shader.setInt("texture2", 2);
	shader.setInt("texture3", 3);

	furnaceOn = false;
	camLightOn = true;
	redstoneLightOn = false;
	
	shader.setBool("furnaceOn", furnaceOn);
	shader.setBool("camLOn", camLightOn);
	shader.setBool("redstoneOn", redstoneLightOn);
	//redstone1
	shader.setVec3("pointLights[0].ambient", glm::vec3(0.05f, 0.0f, 0.0f));
	shader.setVec3("pointLights[0].diffuse", glm::vec3(0.7f, 0.05f, 0.05f));
	shader.setVec3("pointLights[0].specular", glm::vec3(0.4f, 0.1f, 0.1f));
	shader.setFloat("pointLights[0].constant", 1.0f);
	shader.setFloat("pointLights[0].linear", 0.7f);
	shader.setFloat("pointLights[0].quadratic", 1.8f);
	//redstone2
	shader.setVec3("pointLights[1].ambient", glm::vec3(0.05f, 0.0f, 0.0f));
	shader.setVec3("pointLights[1].diffuse", glm::vec3(0.7f, 0.05f, 0.05f));
	shader.setVec3("pointLights[1].specular", glm::vec3(0.4f, 0.1f, 0.1f));
	shader.setFloat("pointLights[1].constant", 1.0f);
	shader.setFloat("pointLights[1].linear", 0.7f);
	shader.setFloat("pointLights[1].quadratic", 1.8f);
	//furnace
	shader.setVec3("pointLights[2].ambient", glm::vec3(0.5f, 0.25f, 0.1f));
	shader.setVec3("pointLights[2].diffuse", glm::vec3(2.5f, 1.25f, 0.5f));
	shader.setVec3("pointLights[2].specular", glm::vec3(2.0f, 1.2f, 0.6f));
	shader.setFloat("pointLights[2].constant", 1.0f);
	shader.setFloat("pointLights[2].linear", 0.09f);
	shader.setFloat("pointLights[2].quadratic", 0.032f);
	//CameraLight
	shader.setVec3("pointLights[3].ambient", glm::vec3(0.3f, 0.3f, 0.3f));
	shader.setVec3("pointLights[3].diffuse", glm::vec3(1.0f, 1.0f, 1.0f));
	shader.setVec3("pointLights[3].specular", glm::vec3(1.0f, 1.0f, 1.0f));
	shader.setFloat("pointLights[3].constant", 1.0f);
	shader.setFloat("pointLights[3].linear", 0.07f);
	shader.setFloat("pointLights[3].quadratic", 0.017f);
}

void mouseCallback(GLFWwindow *window, double xpos, double ypos){
	if(leftMouseButtonPressed){
		if(firstMouse){
			lastX = static_cast<float>(xpos);
			lastY = static_cast<float>(ypos);
			firstMouse = false;
		}
		float xoffset = static_cast<float>(xpos) - lastX;
		float yoffset = lastY - static_cast<float>(ypos);

		lastX = static_cast<float>(xpos);
		lastY = static_cast<float>(ypos);

		camera.ProcessMouseMovement(xoffset, yoffset);
	}else{
		firstMouse = true;
	}
}

void mouseButtonCallback(GLFWwindow *window, int button, int action, int mods){
	if(button == GLFW_MOUSE_BUTTON_LEFT){
		if(action == GLFW_PRESS){
			leftMouseButtonPressed = true;
		}else if(action == GLFW_RELEASE){
			leftMouseButtonPressed = false;
		}
	}
}

void processInput(GLFWwindow *window, Shader &shader)
{
  if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) glfwSetWindowShouldClose(window, true);
  if(glfwGetKey(window, GLFW_KEY_F) == GLFW_PRESS){
	if(!fKeyPressed){
		furnaceOn = !furnaceOn;
		shader.setBool("furnaceOn", furnaceOn);
		fKeyPressed = true;
	}
  }
  if(glfwGetKey(window, GLFW_KEY_F) == GLFW_RELEASE){
	fKeyPressed = false;
  } 
  if(glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS){
	if(minecartOffset < 2.25f) minecartOffset += 0.03125;
  }
  if(glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS){
	if(minecartOffset > 0.0f) minecartOffset -= 0.03125;
  }
  if(glfwGetKey(window, GLFW_KEY_C) == GLFW_PRESS){
	if(!cKeyPressed){
		camLightOn = !camLightOn;
		shader.setBool("camLOn", camLightOn);
		cKeyPressed = true;
	}
  }
  if(glfwGetKey(window, GLFW_KEY_C) == GLFW_RELEASE){
	cKeyPressed = false;
  } 
  if(glfwGetKey(window, GLFW_KEY_V) == GLFW_PRESS){
	if(!vKeyPressed){
		redstoneLightOn = !redstoneLightOn;
		shader.setBool("redstoneOn", redstoneLightOn);
		vKeyPressed = true;
	}
  }
  if(glfwGetKey(window, GLFW_KEY_V) == GLFW_RELEASE){
	vKeyPressed = false;
  } 
}

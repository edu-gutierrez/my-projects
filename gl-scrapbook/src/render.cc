#include "render.hh"

void drawBlock(const Shader &shader, unsigned int VAO, const glm::vec3 &pos, unsigned int textureID, const glm::vec3 &scale){
	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, textureID);
	glm::mat4 model = glm::mat4(1.0f);
	model = glm::translate(model, pos);
	model = glm::scale(model, scale);
	shader.setMat4("modelMatrix", model);
	glDrawArrays(GL_TRIANGLES, 0, 36);
}

void drawEnvironment(const Shader &shader, unsigned int VAO, const Textures &t){
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.4f, 0.4f, 0.4f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, t.stone);
	//Dibujar suelo
	for(float x = -1.5f; x <= 1.5f; x+=0.5f){
		for(float z = -1.5f; z <= 1.5f; z+=0.5f){
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(x, 0.0f, z));
			model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		}	
	}
	//Dibujar pared izquierda
	for(float y = 0.5f; y <= 2.5f; y+=0.5f){
		for(float z = -1.5f; z <= 1.5f; z+=0.5f){
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(-2.0f, y, z));
			model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		}
	}
	//Dibujar pared fondo
	for(float y = 0.5f; y <= 2.5f; y+=0.5f){
		for(float x = -1.5f; x <= 1.5f; x+=0.5f){
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(x, y, -2.0f));
			model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		}
	}
}

void drawRail(const Shader &shader, unsigned int VAO, const Textures &t){
	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, t.cobbledDeepslate);
	glm::vec3 scaleSize = glm::vec3(0.125f, 0.125f, 0.125f);
	for(float x = -1.75f; x < 1.75f; x += 0.125){
		glm::mat4 model = glm::mat4(1.0f);
		model = glm::translate(model, glm::vec3(x, 0.3f, 1.25f));
		model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
		shader.setMat4("modelMatrix", model);
		glDrawArrays(GL_TRIANGLES, 0, 36);
	}
	for(float x = -1.75f; x < 1.75f; x += 0.125){
		glm::mat4 model = glm::mat4(1.0f);
		model = glm::translate(model, glm::vec3(x, 0.3f, 0.75f));
		model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
		shader.setMat4("modelMatrix", model);
		glDrawArrays(GL_TRIANGLES, 0, 36);
	}
	glBindTexture(GL_TEXTURE_2D, t.oakPlanks);
	for(float offset = 0; offset < 3.25; offset += 0.25){
		for(float z = 0.8; z < 1.3; z += 0.1){
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(-1.5f + offset, 0.25f, z));
			model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		}
	}
}

void drawMinecart(const Shader &shader, unsigned int VAO, float offset, const Textures &t){
	shader.setVec4("matAmbient", glm::vec4(0.15f, 0.15f, 0.15f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.6f, 0.6f, 0.6f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(1.0f, 1.0f, 1.0f, 1.0f));
	shader.setFloat("matShininess", 96.0f);
	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, t.ironBlock);
	for(float y = 0.375; y < 0.75; y += 0.125){
		for(float z = 0.8; z < 1.175; z += 0.125){
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(-1.5f + offset, y, z));
			model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		
			model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(-0.75f + offset, y, z));
			model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		}
		for(float x = -1.375; x < -0.75; x += 0.125){
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(x + offset, y, 0.8));
			model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		
			model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3 (x + offset, y, 1.175));
			model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		}
	}

	for(float x = -1.375f; x < -0.75; x += 0.125){
		for(float z = 0.925; z < 1.05; z += 0.125){
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(x + offset, 0.425, z));
			model = glm::scale(model, glm::vec3(0.125f, 0.125f, 0.125f));
			shader.setMat4("modelMatrix", model);
			glDrawArrays(GL_TRIANGLES, 0, 36);
		}
	}
}

void drawRedstoneOres(const Shader &shader, unsigned int VAO, const Textures &t){
	glm::vec3 scaleBlock = glm::vec3(0.5f, 0.5f, 0.5f);
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.1f, 0.1f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.4f, 0.35f, 0.35f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.05f, 0.05f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	drawBlock(shader, VAO, glm::vec3(-1.0f, 0.0f, 0.0f), t.redstoneOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.0f, 0.0f, 1.0f), t.redstoneOre, scaleBlock);
}

void drawCoalOres(const Shader &shader, unsigned int VAO, const Textures &t){
	glm::vec3 scaleBlock = glm::vec3(0.5f, 0.5f, 0.5f);
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.4f, 0.4f, 0.4f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	//Pared1
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.0f, 0.5f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.0f, 1.5f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.0f, 1.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.5f, 1.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.5f, 1.5f), t.coalOre, scaleBlock);
	//Pared2
	drawBlock(shader, VAO, glm::vec3(-1.0f, 1.5f, -2.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-1.0f, 1.0f, -2.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-0.5f, 1.0f, -2.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-0.5f, 2.0f, -2.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-0.5f, 1.5f, -2.0f), t.coalOre, scaleBlock);
	//Suelo
	drawBlock(shader, VAO, glm::vec3(1.0f, 0.0f, 0.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.0f, 0.0f, 0.5f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.0f, 0.0f, 1.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(0.5f, 0.0f, 1.0f), t.coalOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(0.5f, 0.0f, 1.0f), t.coalOre, scaleBlock);
}

void drawIronOres(const Shader &shader, unsigned int VAO, const Textures &t){
	glm::vec3 scaleBlock = glm::vec3(0.5f, 0.5f, 0.5f);
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.4f, 0.4f, 0.4f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	//Pared1
	drawBlock(shader, VAO, glm::vec3(-2.0f, 1.5f, -0.5f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 1.5f, -1.0f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.0f, -1.0f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.0f, -1.5f), t.ironOre, scaleBlock);
	//Pared2
	drawBlock(shader, VAO, glm::vec3(1.0f, 1.5f, -2.0f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.0f, 1.0f, -2.0f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(0.5f, 1.5f, -2.0f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(0.5f, 1.0f, -2.0f), t.ironOre, scaleBlock);
	//Suelo
	drawBlock(shader, VAO, glm::vec3(0.0f, 0.0f, 0.0f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(0.0f, 0.0f, 0.5f), t.ironOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-0.5f, 0.0f, 0.5f), t.ironOre, scaleBlock);
}

void drawGoldOres(const Shader &shader, unsigned int VAO, const Textures &t){
	glm::vec3 scaleBlock = glm::vec3(0.5f, 0.5f, 0.5f);
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.4f, 0.4f, 0.3f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	//Pared1
	drawBlock(shader, VAO, glm::vec3(-2.0f, 0.5f, 0.0f), t.goldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 1.0f, 0.0f), t.goldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 1.0f, -0.5f), t.goldOre, scaleBlock);
	//Pared2
	drawBlock(shader, VAO, glm::vec3(-1.5f, 2.0f, -2.0f), t.goldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-1.0f, 2.0f, -2.0f), t.goldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-1.5f, 2.5f, -2.0f), t.goldOre, scaleBlock);
	//Suelo
	drawBlock(shader, VAO, glm::vec3(-1.0f, 0.0f, -1.5f), t.goldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-0.5f, 0.0f, -1.0f), t.goldOre, scaleBlock);
}

void drawEmeraldOres(const Shader &shader, unsigned int VAO, const Textures &t){
	glm::vec3 scaleBlock = glm::vec3(0.5f, 0.5f, 0.5f);
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.4f, 0.4f, 0.4f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	drawBlock(shader, VAO, glm::vec3(0.5f, 0.0f, -1.5f), t.emeraldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 1.0f, 0.5f), t.emeraldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 2.5f, -1.5f), t.emeraldOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-1.5f, 1.0f, -2.0f), t.emeraldOre, scaleBlock);
}

void drawDiamondOres(const Shader &shader, unsigned int VAO, const Textures &t){
	glm::vec3 scaleBlock = glm::vec3(0.5f, 0.5f, 0.5f);
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.35f, 0.4f, 0.4f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	//Pared1
	drawBlock(shader, VAO, glm::vec3(-2.0f, 0.5f, 1.5f), t.diamondOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 1.0f, 1.5f), t.diamondOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-2.0f, 0.5f, 1.0f), t.diamondOre, scaleBlock);
	//Pared2
	drawBlock(shader, VAO, glm::vec3(1.5f, 2.5f, -2.0f), t.diamondOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.5f, 2.0f, -2.0f), t.diamondOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.0f, 2.5f, -2.0f), t.diamondOre, scaleBlock);
	//Suelo
	drawBlock(shader, VAO, glm::vec3(-1.5f, 0.0f, 1.0f), t.diamondOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(-1.0f, 0.0f, 1.0f), t.diamondOre, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.5f, 0.0f, 1.5f), t.diamondOre, scaleBlock);
}

void drawOres(const Shader &shader, unsigned int VAO, const Textures &t){
	drawRedstoneOres(shader, VAO, t);
	drawCoalOres(shader, VAO, t);
	drawIronOres(shader, VAO, t);
	drawGoldOres(shader, VAO, t);
	drawEmeraldOres(shader, VAO, t);
	drawDiamondOres(shader, VAO, t);
}

void drawFurnaceBlock(const Shader &shader, unsigned int VAO, const Textures &t){
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.8f, 0.8f, 0.8f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, t.furnaceTop);
	glActiveTexture(GL_TEXTURE1);
	glBindTexture(GL_TEXTURE_2D, t.furnaceSide);
	glActiveTexture(GL_TEXTURE2);
	glBindTexture(GL_TEXTURE_2D, t.furnaceFront);
	glActiveTexture(GL_TEXTURE3);
	glBindTexture(GL_TEXTURE_2D, t.furnaceFrontOn);
	bool drawFurnace = true;		
	shader.setBool("drawFurnace", drawFurnace);
	glm::mat4 model = glm::mat4(1.0f);
	model = glm::translate(model, glm::vec3(-1.5f, 0.5f, -1.5f));
	model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));
	shader.setMat4("modelMatrix", model);
	glDrawArrays(GL_TRIANGLES, 0, 36);
	drawFurnace = false;
	shader.setBool("drawFurnace", drawFurnace);
}

void drawShinyBlocks(const Shader &shader, unsigned int VAO, const Textures &t){
	glm::vec3 scaleBlock = glm::vec3(0.5f, 0.5f, 0.5f);
	shader.setVec4("matAmbient", glm::vec4(0.1f, 0.2f, 0.3f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.3f, 0.5f, 0.7f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(1.0f, 1.0f, 1.0f, 1.0f));
	shader.setFloat("matShininess", 128.0f);
	drawBlock(shader, VAO, glm::vec3(1.5f, 0.5f, -1.5f), t.diamondBlock, scaleBlock);
	drawBlock(shader, VAO, glm::vec3(1.5f, 1.0f, -1.5f), t.diamondBlock, scaleBlock);
	shader.setVec4("matAmbient", glm::vec4(0.3f, 0.3f, 0.0f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.7f, 0.7f, 0.5f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(1.0f, 1.0f, 1.0f, 1.0f));
	shader.setFloat("matShininess", 128.0f);
	drawBlock(shader, VAO, glm::vec3(1.0f, 0.5f, -1.5f), t.goldBlock, scaleBlock);
	shader.setVec4("matAmbient", glm::vec4(0.1f, 0.3f, 0.1f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.5f, 0.7f, 0.5f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(1.0f, 1.0f, 1.0f, 1.0f));
	shader.setFloat("matShininess", 128.0f);
	drawBlock(shader, VAO, glm::vec3(1.5f, 0.5f, -1.0f), t.emeraldBlock, scaleBlock);
}

void drawTnt(const Shader &shader, unsigned int VAO, const Textures &t){
	shader.setVec4("matAmbient", glm::vec4(0.2f, 0.2f, 0.2f, 1.0f));
	shader.setVec4("matDiffuse", glm::vec4(0.4f, 0.4f, 0.4f, 1.0f));
	shader.setVec4("matSpecular", glm::vec4(0.1f, 0.1f, 0.1f, 1.0f));
	shader.setFloat("matShininess", 8.0f);
	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, t.tntBottom);
	glActiveTexture(GL_TEXTURE1);
	glBindTexture(GL_TEXTURE_2D, t.tntSide);
	glActiveTexture(GL_TEXTURE2);
	glBindTexture(GL_TEXTURE_2D, t.tntTop);
	bool drawTntB = true;
	shader.setBool("drawTnt", drawTntB);
	glm::mat4 model = glm::mat4(1.0f);
	model = glm::translate(model, glm::vec3(-1.5f, 0.5f, 0.0f));
	model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));
	shader.setMat4("modelMatrix", model);
	glDrawArrays(GL_TRIANGLES, 0, 36);
	model = glm::mat4(1.0f);
	model = glm::translate(model, glm::vec3(-1.5f, 0.5f, 0.5f));
	model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));
	shader.setMat4("modelMatrix", model);
	glDrawArrays(GL_TRIANGLES, 0, 36);
	model = glm::mat4(1.0f);
	model = glm::translate(model, glm::vec3(-1.0f, 0.5f, 0.5f));
	model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));
	shader.setMat4("modelMatrix", model);
	glDrawArrays(GL_TRIANGLES, 0, 36);
	drawTntB = false;
	shader.setBool("drawTnt", drawTntB);
}

void drawObjects(const Shader &shader, unsigned int VAO, const Textures &t){
	drawRail(shader, VAO, t);
	drawShinyBlocks(shader, VAO, t);
	drawFurnaceBlock(shader, VAO, t);
	drawTnt(shader, VAO, t);
}
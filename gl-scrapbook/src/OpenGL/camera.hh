#ifndef CAMERA_H
#define CAMERA_H

#include <glad/glad.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

const float YAW         = -90.0f;
const float PITCH       =  0.0f;
const float DISTANCE    =  6.0f;
const float SENSITIVITY =  0.3f;

class Camera
{
public:
    glm::vec3 targetPosition;
    glm::vec3 position;
    float Yaw;
    float Pitch;

    Camera(glm::vec3 target = glm::vec3(0.0f, 1.5f, 0.0f)) : targetPosition(target), Yaw(YAW), Pitch(PITCH){
                updateCameraVectors();
    }

    glm::mat4 GetViewMatrix(){
        return glm::lookAt(position, targetPosition, glm::vec3(0.0, 1.0, 0.0));
    }

    void ProcessMouseMovement(float xoffset, float yoffset, GLboolean constrainPitch = true){
        xoffset *= SENSITIVITY;
        yoffset *= SENSITIVITY;

        Yaw   += xoffset;
        Pitch += yoffset;

        if (constrainPitch){
            if (Pitch > 89.0f) Pitch = 89.0f;
            if (Pitch < -89.0f) Pitch = -89.0f;
        }

        updateCameraVectors();
    }

private:
    void updateCameraVectors(){
        glm::vec3 direction;
        direction.x = DISTANCE * cos(glm::radians(Yaw)) * cos(glm::radians(Pitch));
        direction.y = DISTANCE * sin(glm::radians(Pitch));
        direction.z = DISTANCE * sin(glm::radians(Yaw)) * cos(glm::radians(Pitch));
        
        position = targetPosition - direction;
    }
};
#endif
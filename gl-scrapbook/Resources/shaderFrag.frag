#version 330 core
out vec4 FragColor;
  
in vec3 N;
in vec3 N_w;
in vec3 P_eye;
in vec2 TexCoord;

uniform sampler2D texture0;
uniform sampler2D texture1;
uniform sampler2D texture2;
uniform sampler2D texture3;
uniform bool drawFurnace;
uniform bool drawTnt;
uniform bool furnaceOn;
uniform bool camLOn;
uniform bool redstoneOn;

uniform vec4 matAmbient;
uniform vec4 matDiffuse;
uniform vec4 matSpecular;
uniform float matShininess;

struct pointLight{
    vec3 position;
    float constant;
    float linear;
    float quadratic;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};
uniform pointLight pointLights[4];

vec4 Phong(vec3 N, vec3 V, pointLight p){
    vec3 L = normalize(p.position - P_eye);

    float distance = length(p.position - P_eye);
    float attenuation = 1.0 / (p.constant + p.linear * distance + p.quadratic * (distance * distance));

    vec4 ambient = matAmbient*vec4(p.ambient, 1.0f);

    float NdotL = max(0.0, dot(N, L));
    vec4 diffuse = matDiffuse * vec4(p.diffuse, 1.0f) * NdotL;

    vec3 R = normalize(2.0 * dot(N, L) * N - L);
    float RdotV = max(0.0, dot(R, V));
    float Ispec = 0;
    if(NdotL > 0){
        Ispec = pow(RdotV, matShininess);
    }
    vec4 specular = matSpecular * vec4(p.specular, 1.0f) * Ispec;
    vec4 color = ambient*attenuation + diffuse*attenuation + specular*attenuation;
    return color;
}

void main()
{
    vec3 V = normalize(-P_eye);
    vec4 totalLight = vec4(0.0);
    if(redstoneOn){
        for(int i = 0; i < 2; ++i){
            totalLight += Phong(N, V, pointLights[i]);
        }
    }
    if(furnaceOn) totalLight += Phong(N, V, pointLights[2]);
    if(camLOn) totalLight += Phong(N, V, pointLights[3]);
    
    if(drawFurnace){      
        if(N_w.x > 0.9f){ //furnace front  
            if(!furnaceOn) FragColor = totalLight * texture(texture2, TexCoord);
            else FragColor = totalLight * texture(texture3, TexCoord);
        }else if(N_w.y > 0.9f || N_w.y < -0.9f){ //Furnace top
            FragColor = totalLight * texture(texture0, TexCoord);
        }else{ //furnace side
            FragColor = totalLight * texture(texture1, TexCoord);
        }
    }else if(drawTnt){
        if(N_w.y > 0.9) FragColor = totalLight * texture(texture2, TexCoord); 
        else if(N_w.y < -0.9) FragColor = totalLight * texture(texture0, TexCoord); 
        else FragColor = totalLight * texture(texture1, TexCoord); 
    }else{
        FragColor = totalLight * texture(texture0, TexCoord);  
    }
} 
